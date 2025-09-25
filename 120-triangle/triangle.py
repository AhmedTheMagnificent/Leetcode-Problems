class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[None] * len(row) for row in triangle]
        def dfs(i, j):
            if i == n - 1:
                return triangle[i][j]
            if memo[i][j] is not None:
                return memo[i][j]
            left = dfs(i + 1, j)
            right = dfs(i + 1, j + 1)
            memo[i][j] = triangle[i][j] + min(left, right)
            return memo[i][j]
        return dfs(0, 0)
        