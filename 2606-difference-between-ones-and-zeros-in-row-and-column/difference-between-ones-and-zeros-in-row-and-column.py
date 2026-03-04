class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        difference_matrix = []
        for i in range(m):
            row = []
            for j in range(n):
                difference = 2 * rows[i] + 2 * cols[j] - m - n
                row.append(difference)
            difference_matrix.append(row)
        return difference_matrix