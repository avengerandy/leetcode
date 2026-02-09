class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.pacificSet = set()
        self.atlanticSet = set()

        for i in range(len(heights)):
            locate = (i, 0)
            self.dfs(self.heights[locate[0]][locate[1]], locate[0], locate[1], 'pacific')

            locate = (i, len(heights[0]) - 1)
            self.dfs(self.heights[locate[0]][locate[1]], locate[0], locate[1], 'atlantic')

        for i in range(len(heights[0])):
            locate = (0, i)
            self.dfs(self.heights[locate[0]][locate[1]], locate[0], locate[1], 'pacific')

            locate = (len(heights) - 1, i)
            self.dfs(self.heights[locate[0]][locate[1]], locate[0], locate[1], 'atlantic')

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                nowLocate = (i, j)
                if nowLocate in self.pacificSet and nowLocate in self.atlanticSet:
                    ans.append(nowLocate)

        return ans

    def dfs(self, prevHeight: int, row: int, col: int, water: str) -> None:
        if row < 0 or col < 0 or row >= len(self.heights) or col >= len(self.heights[0]):
            return

        if water == 'pacific':
            waterSet = self.pacificSet
        else:
            waterSet = self.atlanticSet

        if self.heights[row][col] < prevHeight:
            return

        nowLocate = (row, col)
        if nowLocate in waterSet:
            return
        waterSet.add(nowLocate)

        self.dfs(self.heights[row][col], row + 1, col, water)
        self.dfs(self.heights[row][col], row - 1, col, water)
        self.dfs(self.heights[row][col], row, col + 1, water)
        self.dfs(self.heights[row][col], row, col - 1, water)
