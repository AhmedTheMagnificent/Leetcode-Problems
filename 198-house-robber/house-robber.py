class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = {}

        def dp(i):
            if i < 0:       return 0
            if i == 0:      return nums[0]
            if i in self.memo:   return self.memo[i]

            self.memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
            return self.memo[i]
        return dp(n - 1)
