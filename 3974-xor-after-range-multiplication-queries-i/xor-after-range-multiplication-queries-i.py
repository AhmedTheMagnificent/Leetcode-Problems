class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l, r, k, v = query[:]
            for i in range(l, r + 1, k):    nums[i] = (nums[i] * v) % (10 ** 9 + 7)
        xor = 0
        for num in nums:    xor ^= num
        return xor