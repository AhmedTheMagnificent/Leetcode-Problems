class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        nums.sort()
        n = len(nums)
        for k in range(n - 1, 1, -1):
            i, j = k - 2, k - 1
            if nums[i] + nums[j] > nums[k]:
                perimeter = max(perimeter, nums[i] + nums[j] + nums[k])
        return perimeter