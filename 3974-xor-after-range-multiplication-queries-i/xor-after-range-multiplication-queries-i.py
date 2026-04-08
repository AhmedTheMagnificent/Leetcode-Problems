class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l, r, k, v = query[:]
            while l <= r:
                nums[l] = (nums[l] * v) % (10 ** 9 + 7)
                l += k
        xor = 0
        for num in nums:    xor ^= num
        return xor