# DFS with cache (DP Top-Down)

class Solution:
    memo = {}

    def checkValidString(self, s: str) -> bool:
        self.memo = {}
        return self.check(s, 0, 0)

    def check(self, s: str, index: int, pareCounter: int) -> bool:
        cache = self.memo.get(index * 1000 + pareCounter)
        if cache is not None:
            return cache
        oldPareCounter = pareCounter

        if index == len(s):
            return pareCounter == 0

        for idx in range(index, len(s)):
            chat = s[idx]
            if chat == '(':
                pareCounter = pareCounter + 1
            elif chat == ')':
                if pareCounter == 0:
                    self.memo[index * 1000 + oldPareCounter] = False
                    return False
                else:
                    pareCounter = pareCounter - 1
            elif chat == '*':
                emptyResult = False
                leftResult = False
                rightResult = False
                if pareCounter <= (len(s) - index):
                    emptyResult = self.check(s, idx + 1, pareCounter)
                if pareCounter <= (len(s) - index - 1):
                    leftResult = self.check(s, idx + 1, pareCounter + 1)
                if pareCounter != 0:
                    rightResult = self.check(s, idx + 1, pareCounter - 1)
                self.memo[index * 1000 + oldPareCounter] = emptyResult or leftResult or rightResult
                return emptyResult or leftResult or rightResult

        self.memo[index * 1000 + oldPareCounter] = pareCounter == 0
        return pareCounter == 0
