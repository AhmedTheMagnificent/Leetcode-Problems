class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        total = sum(nums)
        answer = []
        for num in nums:
            rightSum = total - num - leftSum
            answer.append(abs(leftSum - rightSum))
            leftSum += num
        return answer