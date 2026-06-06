class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.dp = [-1] * len(cost)
        return min(self.dfs(0), self.dfs(1))

    def dfs(self, i):
        if i >= len(self.cost):
            return 0
        if self.dp[i] != -1:
            return self.dp[i]
        self.dp[i] = self.cost[i] + min(self.dfs(i + 1), self.dfs(i + 2))
        return self.dp[i]
