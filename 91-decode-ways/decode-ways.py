class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.dp(0, s)

    def dp(self, i, s):
        if i == len(s):         return 1
        if s[i] == "0":         return 0
        if i in self.memo:      return self.memo[i]

        ways = self.dp(i + 1, s)
        if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
            ways += self.dp(i + 2, s)
        self.memo[i] = ways
        return ways

