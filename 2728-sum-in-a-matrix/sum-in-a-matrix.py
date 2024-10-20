class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        for i in range(len(nums[0])):
            maxi = []
            for j in range(len(nums)):
                nums[j] = sorted(nums[j])
                # for k in range(len(nums[0])):
                maxi.append(max(nums[j]))
                nums[j].pop()
            score += max(maxi)
        return score