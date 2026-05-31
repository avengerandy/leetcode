class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.length = len(grid)
        self.time = 0
        self.visited = set()

        # binary search self.time
        minH = 0
        maxH = 0
        for row in range(self.length):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))
        l = minH
        r = maxH
        while l < r:
            self.time = (l + r) >> 1
            if self.dfs(0, 0):
                r = self.time
            else:
                l = self.time + 1
            self.visited = set()

        return r


    def dfs(self, i: int, j: int) -> bool:
        if (i, j) in self.visited:
            return False
        self.visited.add((i, j))

        if i == self.length or j == self.length:
            return False
        if i < 0 or j < 0:
            return False
        if self.grid[i][j] > self.time:
            return False
        if i == self.length - 1 and j == self.length - 1:
            return True

        return (self.dfs(i - 1, j) or
            self.dfs(i + 1, j) or
            self.dfs(i, j + 1) or
            self.dfs(i, j - 1))
