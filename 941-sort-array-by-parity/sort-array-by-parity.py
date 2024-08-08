class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = j = 0
        while j < len(nums):
            if nums[j] % 2 != 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
        return nums