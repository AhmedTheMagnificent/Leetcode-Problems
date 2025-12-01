class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        s = sum(batteries)
        low, high = 0, s // n
        while low < high:
            mid = (low + high + 1) // 2
            total = 0 
            for b in batteries:
                total += min(b, mid)
            if total >= n * mid:
                low = mid

            else:
                high = mid - 1
        return low
