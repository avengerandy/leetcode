class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        numsList = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for lengthOfNums in range(2, n + 2):
            for startIdx in range(n + 2 - lengthOfNums):
                endIdx = startIdx + lengthOfNums
                for idx in range(startIdx + 1, endIdx):
                    tempCoin = dp[startIdx][idx] + dp[idx][endIdx] + numsList[startIdx] * numsList[idx] * numsList[endIdx]
                    dp[startIdx][endIdx] = max(dp[startIdx][endIdx], tempCoin)

        return dp[0][n + 1]
