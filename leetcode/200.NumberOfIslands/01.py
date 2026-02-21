class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ans = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    ans = ans + 1
        return ans

    def dfs(self, i: int, j: int) -> None:
        if i < 0 or j < 0:
            return
        if i > len(self.grid) - 1 or j > len(self.grid[0]) - 1:
            return
        if self.grid[i][j] == '0':
            return
        self.grid[i][j] = '0'
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)
        return
