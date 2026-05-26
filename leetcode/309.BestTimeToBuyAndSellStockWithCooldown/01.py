class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.dp = {}

        return self.dfs(0, True)

    def dfs(self, i, can_buy):
        if i >= len(self.prices):
            return 0
        if (i, can_buy) in self.dp:
            return self.dp[(i, can_buy)]

        do_nothing = self.dfs(i + 1, can_buy)
        if can_buy:
            do_action = self.dfs(i + 1, False) - self.prices[i]
        else:
            do_action = self.dfs(i + 2, True) + self.prices[i]

        self.dp[(i, can_buy)] = max(do_nothing, do_action)
        return self.dp[(i, can_buy)]
