class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numtoindices = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numtoindices:
                return [numtoindices[complement], index]
            numtoindices[num] = index