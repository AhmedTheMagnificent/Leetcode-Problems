class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToKey = {}
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in valueToKey:
                return [i, valueToKey[reminder]]
            valueToKey[nums[i]] = i