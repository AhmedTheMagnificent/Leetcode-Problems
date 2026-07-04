class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = [False] * (n + 1)
        answer = float("inf")
        def dfs(node):
            nonlocal answer
            visited[node] = True
            for neighbour, weight in graph[node]:
                answer = min(answer, weight)
                if not visited[neighbour]: dfs(neighbour)
        dfs(1)
        return answer