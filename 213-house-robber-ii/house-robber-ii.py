class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  return nums[0]

        self.memo = {}
        option1 = self.dp(len(nums) - 2, nums, 0)

        self.memo = {}
        option2 = self.dp(len(nums) - 1, nums, 1)

        return max(option1, option2)

    def dp(self, i, nums, start):
        if i < start:       return 0
        if i == start:      return nums[start]
        if i in self.memo:  return self.memo[i]
        rob_current = self.dp(i - 2, nums, start) + nums[i]
        skip_current = self.dp(i - 1, nums, start)
        self.memo[i] = max(rob_current, skip_current)
        return self.memo[i]