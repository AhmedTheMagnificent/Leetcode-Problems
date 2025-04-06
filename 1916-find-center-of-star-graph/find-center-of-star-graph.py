class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]
        second = edges[1]
        for i in first:
            for j in second:
                if i == j:
                    return i