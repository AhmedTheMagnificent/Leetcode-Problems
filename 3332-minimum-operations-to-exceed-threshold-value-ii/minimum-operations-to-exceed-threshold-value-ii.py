class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        heapq.heapify(nums)
        while nums[0] < k:
            if len(nums) < 2:
                return -1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new = 2 * min(x, y) + max(x, y)
            heapq.heappush(nums, new)
            operations += 1
        return operations