class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for (idx, [x, y, r]) in enumerate(queries):
            for [x1, y1] in points:
                if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                    ans[idx] += 1
        return ans

        