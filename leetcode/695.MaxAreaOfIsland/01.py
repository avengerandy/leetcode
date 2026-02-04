class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        ans = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    area = self.dfs(i, j, 2) - 2
                    ans = max(area, ans)

        return ans

    def dfs(self, i: int, j: int, step: int) -> int:
        if i < 0 or j < 0:
            return step
        if i > len(self.grid) - 1 or j > len(self.grid[0]) - 1:
            return step
        if self.grid[i][j] != 1:
            return step
        self.grid[i][j] = step
        step = step + 1
        step = self.dfs(i + 1, j, step)
        step = self.dfs(i - 1, j, step)
        step = self.dfs(i, j + 1, step)
        return self.dfs(i, j - 1, step)
