from pydantic import BaseSettings
import os
from typing import Optional



class Settings(BaseSettings):
    # Runtime settings
    DEBUG: bool = False
    TESTING: bool = False
    ENV: str = 'development'
    
    # Yara rules directory
    YARA_RULES_DIR_DEV: str = os.path.join('yara_rules', 'yara-rules-yara')
    YARA_RULES_DIR_PROD: str = os.path.join('src', 'yara_rules', 'yara-rules-yara')





settings = Settings()