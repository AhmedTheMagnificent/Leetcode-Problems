class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        incLeft = [1] * len(nums)
        incRight = [1] * len(nums)
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                incLeft[i] = incLeft[i-1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incRight[i] = incRight[i+1] + 1

        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(incLeft[i], incRight[i+1]))
        return ans
        
