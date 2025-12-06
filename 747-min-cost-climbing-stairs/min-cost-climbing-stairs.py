class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        n = len(cost)
        def dp(i):
            if i in self.memo:  return self.memo[i]
            if i <= 1:          return 0
            one_step = dp(i - 1) + cost[i - 1]
            two_steps = dp(i - 2) + cost[i - 2]
            result = min(one_step, two_steps)
            self.memo[i] = result
            return result
        return dp(n)