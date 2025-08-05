class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected = set(range(1, n + 1))
        for i in range(n):
            row = set(matrix[i])
            col = set(matrix[j][i] for j in range(n))
            if row != expected or col != expected:
                return False
        return True
