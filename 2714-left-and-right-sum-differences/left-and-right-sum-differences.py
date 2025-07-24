class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        leftSum = [0] * length
        rightSum = [0] * length
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
            rightSum[-i - 1] = rightSum[-i ] + nums[-i]
        for i in range(length):
            ans.append(abs(leftSum[i] - rightSum[i]))
        return ans