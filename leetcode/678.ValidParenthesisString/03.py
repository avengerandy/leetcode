# DP over all possible open-count states (BFS-style state expansion), memory-optimized

class Solution:
    def checkValidString(self, s: str) -> bool:
        size = len(s)
        memo = [False] * (size + 1)
        memo[0] = True # empty is True

        for idx in range(len(s)):
            newMemo = [False] * (size + 1)
            chat = s[idx]
            for pareCounter in range(size):
                if chat == '(':
                    if pareCounter > 0:
                        newMemo[pareCounter] = memo[pareCounter - 1]
                elif chat == ')':
                    newMemo[pareCounter] = memo[pareCounter + 1]
                else:
                    if pareCounter > 0:
                        newMemo[pareCounter] = (
                            memo[pareCounter + 1] or
                            memo[pareCounter - 1] or
                            memo[pareCounter]
                        )
                    else:
                        newMemo[pareCounter] = (
                            memo[pareCounter + 1] or
                            memo[pareCounter]
                        )
            memo = newMemo

        return memo[0]
