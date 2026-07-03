class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for c in columnTitle:
            num *= 26
            num += ord(c) - ord("A") + 1
        return num