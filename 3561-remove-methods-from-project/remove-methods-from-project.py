class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        suspicious = [False] * n
        def dfs(node):
            suspicious[node] = True
            for neighbour in graph[node]:
                if not suspicious[neighbour]:
                    dfs(neighbour)
        dfs(k)
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i]]
        