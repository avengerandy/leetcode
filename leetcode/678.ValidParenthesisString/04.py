# Stack Greedy

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        for idx in range(len(s)):
            char = s[idx]
            if char == '(':
                leftStack.append(idx)
            elif char == '*':
                starStack.append(idx)
            else:
                if len(leftStack):
                    leftStack.pop()
                elif len(starStack):
                    starStack.pop()
                else:
                    return False

        if len(leftStack) > len(starStack):
            return False

        for idx in range(len(leftStack)-1, -1, -1):
            if leftStack[idx] > starStack.pop():
                return False

        return True
