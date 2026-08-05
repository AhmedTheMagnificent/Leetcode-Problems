class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m * n
        ops.sort(key=lambda x: (x[0], x[1]))
        return min(a for a, _ in ops) * min(b for _, b in ops)