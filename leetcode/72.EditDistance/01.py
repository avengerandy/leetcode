class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.dp = {}
        return self.dfs(0, 0)

    def dfs(self, i, j) -> int:
        if i == len(self.word1):
            return len(self.word2) - j
        if j == len(self.word2):
            return len(self.word1) - i

        if (i, j) in self.dp:
            return self.dp[(i, j)]

        if self.word1[i] == self.word2[j]:
            self.dp[(i, j)] = self.dfs(i + 1, j + 1)
        else:
            # Insert/Delete
            res = min(self.dfs(i + 1, j), self.dfs(i, j + 1))
            # Replace
            res = min(res, self.dfs(i + 1, j + 1))
            # action add 1
            self.dp[(i, j)] = res + 1
        return self.dp[(i, j)]
