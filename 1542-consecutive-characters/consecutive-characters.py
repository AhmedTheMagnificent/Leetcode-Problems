class Solution:
    def maxPower(self, s: str) -> int:
        length = 1
        maxlength = 1
        for i in range(len(s)-1):
            if s[i] == s[i + 1]:
                length += 1
            else:
                length = 1
            maxlength = max(maxlength, length)
        return maxlength