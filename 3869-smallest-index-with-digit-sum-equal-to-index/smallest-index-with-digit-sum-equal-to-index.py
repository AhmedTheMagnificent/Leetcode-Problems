class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            num = 0
            while n > 0:
                num += n % 10
                n //= 10
            if i == num:    return i
        return -1