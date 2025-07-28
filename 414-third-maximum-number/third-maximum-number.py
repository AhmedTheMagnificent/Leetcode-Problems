class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        return nums[2] if 3 <= len(nums) else nums[0]