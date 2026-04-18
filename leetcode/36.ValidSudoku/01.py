class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # isRowValid
        for row in board:
            cache = set()
            for num in row:
                if num != '.' and num in cache:
                    return False
                cache.add(num)

        # isColValid
        for idx in range(9):
            cache = set()
            for row in board:
                if row[idx] != '.' and row[idx] in cache:
                    return False
                cache.add(row[idx])

        # isBlockValid
        for iBlock in range(3):
            for jBlock in range(3):
                cache = set()
                for i in range(3):
                    for j in range(3):
                        idx = iBlock * 3 + i
                        jdx = jBlock * 3 + j
                        if board[idx][jdx] != '.' and board[idx][jdx] in cache:
                            return False
                        cache.add(board[idx][jdx])

        return True
