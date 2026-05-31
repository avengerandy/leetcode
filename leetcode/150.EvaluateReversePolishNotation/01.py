class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in ['+', '-', '*', '/']:
                number2 = stack.pop()
                number1 = stack.pop()
                ans = None
                if char == '+':
                    ans = number1 + number2
                if char == '-':
                    ans = number1 - number2
                if char == '*':
                    ans = number1 * number2
                if char == '/':
                    ans = int(number1 / number2)
                stack.append(ans)
            else:
                stack.append(int(char))

        return stack[0]
