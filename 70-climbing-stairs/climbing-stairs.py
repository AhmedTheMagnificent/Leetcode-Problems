class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)

    def dp(self, n):
        if n in self.memo:  return self.memo[n]
        if n == 0:          return 1
        if n < 0:           return 0
        result = self.dp(n - 1) + self.dp(n - 2)
        self.memo[n] = result
        return result

        