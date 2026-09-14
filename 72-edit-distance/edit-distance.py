class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # dp[i][j] will hold the min operations to convert word1[0..i-1] to word2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base Cases: converting a string to an empty string requires deletions
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match; no new operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose the minimum operations among:
                    # 1. Delete: dp[i - 1][j] + 1
                    # 2. Insert: dp[i][j - 1] + 1
                    # 3. Replace: dp[i - 1][j - 1] + 1
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        return dp[m][n]