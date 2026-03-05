class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mis1, mis2 = 0, 0
        for i in range(n):
            if int(s[i]) != i % 2:
                mis1 += 1
            else:
                mis2 += 1
        return min(mis1, mis2)