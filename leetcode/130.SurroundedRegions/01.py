class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.visited = set()
        wallOlocations = []
        for i in range(len(self.board)):
            wallOlocations.append((i, 0))
            wallOlocations.append((i, len(self.board[i]) - 1))

        for j in range(len(self.board[i])):
            wallOlocations.append((0, j))
            wallOlocations.append((len(self.board) - 1, j))

        for wallOlocation in wallOlocations:
            self.dfs(wallOlocation[0], wallOlocation[1])

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '#':
                    self.board[i][j] = 'O'
                elif self.board[i][j] == 'O':
                    self.board[i][j] = 'X'

    def dfs(self, i: int, j: int):
        if i < 0 or j < 0:
            return
        if i > len(self.board) - 1 or j > len(self.board[0]) - 1:
            return
        if self.board[i][j] == 'X':
            return
        if (i, j) in self.visited:
            return
        self.visited.add((i, j))
        self.board[i][j] = '#'

        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)
