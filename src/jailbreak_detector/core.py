from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict
from .matcher import AhoCorasickMatcher
from .patterns import PatternManager

@dataclass
class DetectionResult:
    is_jailbreak: bool
    matched_patterns: List[Dict]
    confidence: str
    categories: List[str]

class JailbreakDetector:
    def __init__(self, pattern_file=None):
        if pattern_file is None:
            pattern_file = Path(__file__).parent.parent.parent / "data" / "patterns.json"

        self.pattern_manager = PatternManager()
        self.pattern_manager.load_from_json(pattern_file)

        self.matcher = AhoCorasickMatcher(case_sensitive=False)
        for pattern, category in self.pattern_manager.get_all_patterns():
            self.matcher.add_pattern(pattern, {"category": category})
        self.matcher.build()

    def detect(self, text):
        matches = self.matcher.search(text)

        if not matches:
            return DetectionResult(
                is_jailbreak=False,
                matched_patterns=[],
                confidence="NONE",
                categories=[]
            )

        categories = list(set(m["metadata"]["category"] for m in matches))
        confidence = "HIGH" if len(matches) >= 2 else "MEDIUM"

        return DetectionResult(
            is_jailbreak=True,
            matched_patterns=matches,
            confidence=confidence,
            categories=categories
        )
