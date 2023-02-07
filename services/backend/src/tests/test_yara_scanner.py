# Path: tests/test_yara_scanner.py

from app.yara_scanner import YaraScanner


def test_yara_scanner():
    yara_scanner = YaraScanner()
    assert yara_scanner is not None


def test_yara_scanner_scan_string():
    yara_scanner = YaraScanner()
    yara_scanner.compile()
    result = yara_scanner.scan_string("test")
    assert result is not None