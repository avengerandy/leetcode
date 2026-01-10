# DFS

class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.check(s, 0, 0)

    def check(self, s: str, index: int, pareCounter: int) -> bool:
        if index == len(s):
            return pareCounter == 0

        for idx in range(index, len(s)):
            chat = s[idx]
            if chat == '(':
                pareCounter = pareCounter + 1
            elif chat == ')':
                if pareCounter == 0:
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
                return emptyResult or leftResult or rightResult

        return pareCounter == 0
