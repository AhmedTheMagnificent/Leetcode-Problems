class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxIndex = 0
        maxNumber = -float('inf')
        for i, num in enumerate(nums):
            if num > maxNumber:
                maxNumber = num
                maxIndex = i
        for num in nums:
            if num != maxNumber and maxNumber < 2 * num:
                return -1
        return maxIndex