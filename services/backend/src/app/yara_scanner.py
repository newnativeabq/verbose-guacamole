"""
Yara Helper Functions
"""

import os
import yara

from .config import settings



class YaraScanner():
    
    def __init__(self, rules_dir=None):
        if rules_dir is None:
            if settings.ENV == 'production':
                rules_dir = settings.YARA_RULES_DIR_PROD
            elif settings.ENV == 'development':
                rules_dir = settings.YARA_RULES_DIR_DEV

        self.rules_dir = rules_dir
        self._rules = None
        self.compile()


    def _load_yara_rules(self) -> dict:

        def _scan_for_index_or_available(rules_files: list) -> dict:
            rules_dict = {}
            index = {}
            for f in rules_files:
                if f == "index.yar":
                    index[f] = os.path.join(self.rules_dir, f)
                    return index
                elif f.endswith(".yar"):
                    rules_dict[f] = os.path.join(self.rules_dir, f)
            return rules_dict

        if os.path.isdir(self.rules_dir) is False:
            local_absolute_path = os.path.join(os.getcwd(), self.rules_dir)
            if os.path.isdir(local_absolute_path):
                self.rules_dir = local_absolute_path
            else:
                raise Exception("Rules directory does not exist: {}".format(self.rules_dir))
        
        rules_files = os.listdir(self.rules_dir)

        if len(rules_files) == 0:
            raise Exception("No rules found in directory: {}".format(self.rules_dir))
        
        rules_dict = _scan_for_index_or_available(rules_files)

        return rules_dict


    def compile(self):
        rules_dict = self._load_yara_rules()

        if len(rules_dict) == 1:
            fpath = rules_dict.popitem()[1]
            assert os.path.exists(fpath), "Rule file does not exist: {}".format(fpath)
            self._rules = yara.compile(filepath=fpath)
        elif len(rules_dict) > 1:
            self._rules = yara.compile(filepaths=rules_dict)


    def scan_string(self, string: str):
        return self._rules.match(data=string)
    


default_scanner = YaraScanner()
default_scanner.compile()