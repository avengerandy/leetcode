class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coinCounter = [0] * (amount + 1)
        coinCounter[0] = 1

        for coin in coins:
            for i in range(amount + 1):
                if coin > i:
                    continue
                remaind = i - coin
                coinCounter[i] = coinCounter[i] + coinCounter[remaind]

        return coinCounter[-1]
