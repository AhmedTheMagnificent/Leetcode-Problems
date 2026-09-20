class Solution:
    def reverseDegree(self, s: str) -> int:
        mapp = {
            chr(i): 123 - i
            for i in range(97, 123)
        }
        degree = 0
        for i in range(1, len(s) + 1):
            degree += i * mapp[s[i - 1]]
        return degree