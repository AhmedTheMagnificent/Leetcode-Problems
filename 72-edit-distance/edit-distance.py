class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ins_cost, del_cost, rep_cost = 1, 1, 1
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + del_cost
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ins_cost
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + ins_cost,
                        dp[i - 1][j] + del_cost,
                        dp[i - 1][j - 1] + rep_cost
                    )
        return dp[m][n]
