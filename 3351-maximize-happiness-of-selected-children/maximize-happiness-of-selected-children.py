class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        maxHeap = [-h for h in happiness]
        priority_queue = heapq.heapify(maxHeap)
        value = 0
        for i in range(k):
            curr = -heapq.heappop(maxHeap) - i
            if curr <= 0: break
            value += curr
        return value