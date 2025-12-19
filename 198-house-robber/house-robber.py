class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.dp(len(nums) - 1, nums)

    def dp(self, i, nums):
        if i < 0:   return 0
        if i == 0:  return nums[0]
        if i in self.memo:  return self.memo[i]
        rob_current = nums[i] + self.dp(i - 2, nums)
        skip_current = self.dp(i - 1, nums)
        result = max(rob_current, skip_current)
        self.memo[i] = result
        return result