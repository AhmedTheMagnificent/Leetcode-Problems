class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                v = grid[i][j]
                count += 1 if v > 0 else 0
        for i in range(len(grid)):
            count += max(grid[i])
        for i in range(len(grid)):
            maxCols = 0
            for j in range(len(grid)):
                cols = grid[j][i]
                maxCols = max(cols, maxCols)
            count += maxCols

        return count