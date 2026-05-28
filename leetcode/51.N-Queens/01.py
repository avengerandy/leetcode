import itertools

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.ans = []
        searchSpace = itertools.permutations(range(n))
        for solution in searchSpace:
            if self.checkAns(solution):
                self.addAns(solution)

        return self.ans

    def addAns(self, solution: List[int]) -> None:
        tempAns = []
        for queenIdx in solution:
            chessRow = ['.'] * self.n
            chessRow[queenIdx] = 'Q'
            tempAns.append(''.join(chessRow))
        self.ans.append(tempAns)

    def checkAns(self, solution: List[int]) -> bool:
        leftCache = set()
        rightCache = set()
        for idx in range(len(solution)):
            queenIdx = solution[idx]
            left = queenIdx - idx
            right = queenIdx + idx
            if left in leftCache or right in rightCache:
                return False
            leftCache.add(left)
            rightCache.add(right)
        return True
