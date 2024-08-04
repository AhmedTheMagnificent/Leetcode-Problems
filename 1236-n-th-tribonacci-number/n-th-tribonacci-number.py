class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            memo[n] =  self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return memo[n]
        