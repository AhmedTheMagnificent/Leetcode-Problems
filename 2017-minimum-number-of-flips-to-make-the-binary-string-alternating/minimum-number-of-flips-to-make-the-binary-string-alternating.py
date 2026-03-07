class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        diff1, diff2 = 0, 0
        ans = float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] != str(r % 2):
                diff1 += 1
            if s[r] != str((r + 1) % 2):
                diff2 += 1
            if r - l + 1 > n:
                if s[l] != str(l % 2):
                    diff1 -= 1
                if s[l] != str((l + 1) % 2):
                    diff2 -= 1
                l += 1
            if r - l + 1 == n: ans = min(ans, diff1, diff2)
        return ans