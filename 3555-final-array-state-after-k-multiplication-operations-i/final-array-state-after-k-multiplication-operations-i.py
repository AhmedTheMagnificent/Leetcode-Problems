class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minIndex = nums.index(min(nums))
            nums[minIndex] *= multiplier
        return nums