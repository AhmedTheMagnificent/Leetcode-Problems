class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        output = [0] * len(nums)
        i = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                number = nums[left] ** 2
                left += 1
            else:
                number = nums[right] ** 2
                right -= 1
            output[i] = number
            i -= 1
        return output