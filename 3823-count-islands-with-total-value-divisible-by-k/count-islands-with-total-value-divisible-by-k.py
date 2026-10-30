class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        n, m = len(grid[0]), len(grid)
        count = 0
        def bfs(i, j):
            q = deque([(i, j)])
            visited[i][j] = True
            total = 0
            while q:
                x, y = q.popleft()
                total += grid[x][y]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n
                        and grid[nx][ny] > 0
                        and not visited[nx][ny]
                        ):
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return total
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    total = bfs(i, j)
                    if total % k == 0:  count += 1
        return count
