import pytest
from jailbreak_detector.matcher import AhoCorasickMatcher

def test_basic_match():
    matcher = AhoCorasickMatcher()
    matcher.add_pattern("test", {"category": "test_cat"})
    matcher.build()

    results = matcher.search("this is a test")
    assert len(results) == 1
    assert results[0]["pattern"] == "test"

def test_case_insensitive():
    matcher = AhoCorasickMatcher(case_sensitive=False)
    matcher.add_pattern("test", {"category": "test_cat"})
    matcher.build()

    results = matcher.search("this is a TEST")
    assert len(results) == 1

def test_multiple_patterns():
    matcher = AhoCorasickMatcher()
    matcher.add_pattern("foo", {"category": "cat1"})
    matcher.add_pattern("bar", {"category": "cat2"})
    matcher.build()

    results = matcher.search("foo and bar")
    assert len(results) == 2

def test_no_match():
    matcher = AhoCorasickMatcher()
    matcher.add_pattern("test", {"category": "test_cat"})
    matcher.build()

    results = matcher.search("nothing here")
    assert len(results) == 0
