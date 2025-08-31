class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            idx = sorted_nums.index(nums[i])
            nums[i] = idx
        return nums