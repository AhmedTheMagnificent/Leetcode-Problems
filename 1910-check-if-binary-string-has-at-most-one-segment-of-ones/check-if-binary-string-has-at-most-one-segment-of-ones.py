class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev = 1
        for i in range(1, len(s)):
            if s[i] == "1" and prev == 0:   return False
            elif s[i] == "1" and prev == 1:   prev = 1

            else:   prev = 0
        return True
