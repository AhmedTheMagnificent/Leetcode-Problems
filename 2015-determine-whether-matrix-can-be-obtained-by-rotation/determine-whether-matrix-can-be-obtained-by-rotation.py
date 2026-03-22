class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m, n = len(mat), len(mat[0])
        for _ in range(4):
            if mat == target:   return True
            mat = [list(m) for m in zip(*mat[::-1])]

        return False