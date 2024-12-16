class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        ret = [0] * len(nums)
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        for i in range(k):
            num, idx = heapq.heappop(heap)
            num *= multiplier
            heapq.heappush(heap, (num, idx))
        
        for num, idx in heap:
            ret[idx] = num
        return ret
        