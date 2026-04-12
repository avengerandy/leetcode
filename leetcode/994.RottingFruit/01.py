class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rots = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rots.append((i, j))

        if len(rots) == (len(grid) * len(grid[0])):
            return 0

        counter = 0
        while len(rots):
            counter = counter + 1
            newRots = []
            for location in rots:
                i = location[0]
                j = location[1]
                if i > 0 and grid[i - 1][j] == 1:
                    newRots.append((i - 1, j))
                    grid[i - 1][j] = 2
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    newRots.append((i + 1, j))
                    grid[i + 1][j] = 2
                if j > 0 and grid[i][j - 1] == 1:
                    newRots.append((i, j - 1))
                    grid[i][j - 1] = 2
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    newRots.append((i, j + 1))
                    grid[i][j + 1] = 2
            rots = newRots

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return max(0, counter - 1)
