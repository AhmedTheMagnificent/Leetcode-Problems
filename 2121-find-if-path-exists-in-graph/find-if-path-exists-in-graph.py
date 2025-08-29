class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
            graph[u].append(v)
        
        visited = [False] * n
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if not visited[node]:
                visited[node] = True
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        stack.append(neighbour)

        return False
    