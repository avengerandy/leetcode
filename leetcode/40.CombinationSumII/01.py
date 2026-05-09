class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = candidates
        self.candidates.sort()
        self.dfs(target, [], 0)
        return self.ans

    def dfs(self, target: int, memory: List[int], numIdx: int) -> None:
        for idx in range(numIdx, len(self.candidates)):
            if idx > numIdx and self.candidates[idx] == self.candidates[idx-1]:
                continue
            candidate = self.candidates[idx]
            if target - candidate == 0:
                memory.append(candidate)
                self.ans.append(memory.copy())
                memory.pop()
                continue
            if target - candidate < 0:
                break
            memory.append(candidate)
            self.dfs(target - candidate, memory, idx + 1)
            memory.pop()
