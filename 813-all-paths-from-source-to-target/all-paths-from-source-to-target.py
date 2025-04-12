class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []

        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                result.append(list(path))
            else:
                for neighbours in graph[node]:
                    dfs(neighbours)
            path.pop()
        dfs(0)
        return result

