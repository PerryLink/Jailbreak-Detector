import json
from pathlib import Path

class PatternManager:
    def __init__(self):
        self.patterns = {}

    def load_from_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.patterns = json.load(f)
        return self

    def get_patterns_by_category(self, category=None):
        if category:
            return self.patterns.get(category, [])
        return self.patterns

    def get_all_patterns(self):
        all_patterns = []
        for category, patterns in self.patterns.items():
            for pattern in patterns:
                all_patterns.append((pattern, category))
        return all_patterns

    def add_pattern(self, category, pattern):
        if category not in self.patterns:
            self.patterns[category] = []
        if pattern not in self.patterns[category]:
            self.patterns[category].append(pattern)

    def save_to_json(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.patterns, f, indent=2, ensure_ascii=False)
