class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numToIndex:
                return [i, numToIndex[complement]]
            numToIndex[nums[i]] = i
            