class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numtoindex = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numtoindex:
                return [numtoindex[complement], i]
            else:
                numtoindex[nums[i]] = i