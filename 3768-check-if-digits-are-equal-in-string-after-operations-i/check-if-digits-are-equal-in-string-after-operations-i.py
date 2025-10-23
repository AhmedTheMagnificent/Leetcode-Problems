class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            l = len(s)
            for i in range(len(s) - 1):
                s += str((int(s[i]) + int(s[i + 1])) % 10)
            s = s[l:]
        return s[0] == s[1]