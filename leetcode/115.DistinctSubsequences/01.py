class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        self.s = s
        self.t = t
        self.dp = {}

        return self.dfs(0, 0)

    def dfs(self, sIdx: int, tIdx: int) -> int:
        if tIdx == len(self.t):
            return 1
        if sIdx == len(self.s):
            return 0
        if (sIdx, tIdx) in self.dp:
            return self.dp[(sIdx, tIdx)]

        notTakeCount = self.dfs(sIdx + 1, tIdx)
        takeCount = 0
        if self.s[sIdx] == self.t[tIdx]:
            takeCount = self.dfs(sIdx + 1, tIdx + 1)

        self.dp[(sIdx, tIdx)] = notTakeCount + takeCount
        return self.dp[(sIdx, tIdx)]
