class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    ans = 1
                else:
                    ans = ans + dp[j]
                    dp[j] = ans
        return ans
