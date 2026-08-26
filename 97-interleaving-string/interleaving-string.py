class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        # Length check invariant
        if m + n != len(s3):
            return False

        # Optimize space: ensure s2 is the shorter string to use O(min(m, n)) space
        if m < n:
            return self.isInterleave(s2, s1, s3)

        # dp[j] represents whether s3[:i+j] can be formed by s1[:i] and s2[:j]
        dp = [False] * (n + 1)
        dp[0] = True

        # Base case initialization for matching s2 with s3 (when s1 is empty)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the DP array line by line
        for i in range(1, m + 1):
            # Base case for matching s1 with s3 (when s2 is empty)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2

        return dp[n]