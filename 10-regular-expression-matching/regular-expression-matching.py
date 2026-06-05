class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        def dp(i, j):
            if j == n:  return i == m
            firstMatch = i < m and (s[i] == p[j] or p[j] == ".")
            if j + 1 < n and p[j + 1] == "*":
                return dp(i, j + 2) or (firstMatch and dp(i + 1, j))
            return firstMatch and dp(i + 1, j + 1) 
        return dp(0, 0)