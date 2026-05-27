class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            # visited
            board[r][c] = "#"

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            board[r][c] = char

            if not curr_node.children:
                parent_node.children.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res
