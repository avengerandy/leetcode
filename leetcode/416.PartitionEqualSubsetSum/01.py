class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        self.target = target / 2
        self.nums = nums
        self.nums.sort()
        self.dp = dict()

        return self.dfs(0, 0)

    def dfs(self, idx: int, totalSum: int) -> bool:
        totalSumWithIdx = self.nums[idx] + totalSum
        if totalSumWithIdx == self.target:
            return True
        if idx == len(self.nums) - 1:
            return False
        if totalSumWithIdx > self.target:
            return False
        if (idx, totalSum) in self.dp:
            return self.dp[(idx, totalSum)]
        ans = self.dfs(idx + 1, totalSum) or self.dfs(idx + 1, totalSumWithIdx)
        self.dp[(idx, totalSum)] = ans
        return ans
