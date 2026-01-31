class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.dfs(target, [], 0)
        return self.ans

    def dfs(self, target: int, memory: List[int], numIdx: int) -> None:
        for idx in range(numIdx, len(self.nums)):
            num = self.nums[idx]
            if target - num == 0:
                memory.append(num)
                self.ans.append(memory.copy())
                memory.pop()
                continue
            if target - num < 0:
                continue
            memory.append(num)
            self.dfs(target - num, memory, idx)
            memory.pop()
