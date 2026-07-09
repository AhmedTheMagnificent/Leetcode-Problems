class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        components = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                components[i] = components[i - 1]
            else:
                components[i] = components[i - 1] + 1
        return [components[u] == components[v] for u, v in queries]