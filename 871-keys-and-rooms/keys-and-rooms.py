class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        rooms = {i: room for i, room in enumerate(rooms)}
        visited = [False for _ in range(n)]

        stack = [0]
        visited[0] = True
        while stack:
            node = stack.pop()
            visited[node] = True
            for neighbour in rooms[node]:
                if visited[neighbour] != True:
                    visited[neighbour] = True
                    stack.append(neighbour)
        ans = True
        for nodes in visited:
            ans &= nodes
        return ans