class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f, l = 0, len(nums) - 1
        while f <= l:
            if nums[l] == 0:
                l -= 1
            elif nums[f] == 0:
                for i in range(l - f):
                    nums[f+i] = nums[f+i+1]
                nums[l] = 0
                l-=1
            else:
                f += 1
            
