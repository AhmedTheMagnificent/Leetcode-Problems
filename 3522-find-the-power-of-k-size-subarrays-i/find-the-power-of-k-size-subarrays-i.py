class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = k - 1
        ret = []
        while j < len(nums):
            ret.append(self.helper(nums, i, j))
            i += 1
            j += 1
        return ret


    def helper(self, nums, i, j):
        for k in range(i, j):
            if nums[k] != nums[k+1] - 1:
                return -1
        return nums[j]