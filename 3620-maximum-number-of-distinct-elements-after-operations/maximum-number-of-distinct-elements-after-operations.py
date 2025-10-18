class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        nextAvailable = -float("inf")
        for num in nums:
            start = num - k
            end = num + k
            pick = max(start, nextAvailable)
            if pick <= end:
                count += 1
                nextAvailable = pick + 1
        return count