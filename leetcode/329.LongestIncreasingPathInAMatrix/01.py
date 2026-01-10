class Solution:

    cache = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0

        iSize = len(matrix)
        jSize = len(matrix[0])
        self.cache = [[0] * jSize for _ in range(iSize)]

        for i in range(iSize):
            for j in range(jSize):
                self.dfs(matrix, i, j)

        return max(map(max, self.cache))

    def dfs(self, matrix: List[List[int]], i: int, j : int) -> int:
        if self.cache[i][j] != 0:
            return self.cache[i][j]

        iSize = len(matrix)
        jSize = len(matrix[0])

        ans = 0
        if i != 0 and matrix[i][j] < matrix[i-1][j]:
            ans = max(ans, self.dfs(matrix, i-1, j))
        if i != (iSize - 1) and matrix[i][j] < matrix[i+1][j]:
            ans = max(ans, self.dfs(matrix, i+1, j))
        if j != 0 and matrix[i][j] < matrix[i][j-1]:
            ans = max(ans, self.dfs(matrix, i, j-1))
        if j != (jSize - 1) and matrix[i][j] < matrix[i][j+1]:
            ans = max(ans, self.dfs(matrix, i, j+1))

        selfStep = 1
        self.cache[i][j] = ans + selfStep
        return self.cache[i][j]
