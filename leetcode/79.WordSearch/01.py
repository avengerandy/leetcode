class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.visited = set()

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, i: int, j: int, idx: int) -> bool:
        if idx == len(self.word):
            return True

        if i < 0 or j < 0:
            return False

        if i >= len(self.board) or j >= len(self.board[0]) :
            return False

        if self.word[idx] != self.board[i][j]:
            return False

        if (i, j) in self.visited:
            return False

        self.visited.add((i, j))
        down = self.dfs(i + 1, j, idx + 1)
        top = self.dfs(i - 1, j, idx + 1)
        right = self.dfs(i, j + 1, idx + 1)
        left = self.dfs(i, j - 1, idx + 1)

        self.visited.remove((i, j))

        return down or top or right or left

