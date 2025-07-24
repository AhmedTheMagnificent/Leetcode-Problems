class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            leftSum = sum([num for num in nums[:i]])
            rightSum = sum([num for num in nums[i + 1:]])
            ans.append(abs(leftSum - rightSum))
        return ans