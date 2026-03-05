import pytest
import tempfile
import json
from pathlib import Path
from jailbreak_detector.patterns import PatternManager

def test_load_patterns():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump({"test_cat": ["pattern1", "pattern2"]}, f)
        temp_file = f.name

    pm = PatternManager()
    pm.load_from_json(temp_file)

    assert "test_cat" in pm.patterns
    assert len(pm.patterns["test_cat"]) == 2

    Path(temp_file).unlink()

def test_add_pattern():
    pm = PatternManager()
    pm.add_pattern("new_cat", "new_pattern")

    assert "new_cat" in pm.patterns
    assert "new_pattern" in pm.patterns["new_cat"]

def test_get_all_patterns():
    pm = PatternManager()
    pm.patterns = {"cat1": ["p1", "p2"], "cat2": ["p3"]}

    all_patterns = pm.get_all_patterns()
    assert len(all_patterns) == 3
