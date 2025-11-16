class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        m = 0
        for c in s:
            if c == "1":
                m += 1
            else:
                count += m * (m + 1) // 2
                m = 0
        count += m * (m + 1) // 2
        return count % (10 ** 9 + 7)