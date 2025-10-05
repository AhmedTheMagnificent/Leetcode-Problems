class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        low = nums[0] * nums[1] * nums[-1]
        high = nums[-1] * nums[-2] * nums[-3]
        return max(low, high)