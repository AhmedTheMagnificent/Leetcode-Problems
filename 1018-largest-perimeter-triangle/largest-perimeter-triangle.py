class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for k in range(n - 1, 1, -1):
            i, j = k - 2, k - 1
            if nums[i] + nums[j] > nums[k]:
                return nums[i] + nums[j] + nums[k]
        return 0