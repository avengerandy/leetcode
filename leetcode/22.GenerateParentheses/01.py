class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        self.oneStep(n, n, '', parentheses)
        return parentheses

    def oneStep(
        self,
        openParenthesesSize: int,
        closeParenthesesSize: int,
        parenthesis: str,
        parentheses: List[str]
    ):
        if openParenthesesSize == 0 and closeParenthesesSize == 0:
            parentheses.append(parenthesis)
            return

        if openParenthesesSize > 0:
            self.oneStep(
                openParenthesesSize - 1,
                closeParenthesesSize,
                parenthesis + '(',
                parentheses
            )
        if closeParenthesesSize > openParenthesesSize:
            self.oneStep(
                openParenthesesSize,
                closeParenthesesSize - 1,
                parenthesis + ')',
                parentheses
            )

        return parentheses
