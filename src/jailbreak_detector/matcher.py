import ahocorasick

class AhoCorasickMatcher:
    def __init__(self, case_sensitive=False):
        self.automaton = ahocorasick.Automaton()
        self.case_sensitive = case_sensitive
        self._built = False

    def add_pattern(self, pattern, metadata=None):
        key = pattern if self.case_sensitive else pattern.lower()
        self.automaton.add_word(key, (pattern, metadata))
        self._built = False

    def build(self):
        self.automaton.make_automaton()
        self._built = True

    def search(self, text):
        if not self._built:
            raise RuntimeError("Must call build() before search()")

        search_text = text if self.case_sensitive else text.lower()
        results = []

        for end_pos, (pattern, metadata) in self.automaton.iter(search_text):
            start_pos = end_pos - len(pattern) + 1
            results.append({
                "pattern": pattern,
                "start": start_pos,
                "end": end_pos + 1,
                "metadata": metadata
            })

        return results
