class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        mapping = {}
        reverseMapping = {}
        for p, word in zip(pattern, s):
            if p not in mapping and word not in reverseMapping:
                mapping[p] = word
                reverseMapping[word] = p
            elif mapping.get(p) != word:
                return False
        return True