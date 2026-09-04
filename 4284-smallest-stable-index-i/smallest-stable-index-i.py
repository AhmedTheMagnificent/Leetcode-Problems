class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        output = []
        for i in range(len(nums)):
            ma = max(nums[0: i + 1])
            mi = min(nums[i: len(nums)])
            if ma - mi <= k:    return i
        return -1