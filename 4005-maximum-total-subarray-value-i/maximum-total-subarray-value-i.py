class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maximum, minimum = max(nums), min(nums)
        return (maximum - minimum) * k