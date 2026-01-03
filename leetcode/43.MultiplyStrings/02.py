# Multi-digit multiplication using multiplication and addition.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        return self.mul(num1, num2)

    def mul(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.mul(num2, num1)

        ans = '0'
        num1Len = len(num1)
        num2Len = len(num2)
        if num2Len > 1:
            for i in range(num2Len):
                temp = self.mul(num1, num2[num2Len - i - 1])
                ans = self.add(temp + '0' * i, ans)
        else:
            ans = ''
            num2Number = int(num2[0])
            carry = '0'
            for i in range(num1Len):
                temp = str(int(num1[num1Len - i - 1]) * num2Number + int(carry))
                carry = '0'
                if len(temp) > 1:
                    carry = temp[0]
                    ans = temp[1] + ans
                else:
                    ans = temp[0] + ans
            if carry != '0':
                ans = carry + ans
        return ans

    def add(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.add(num2, num1)

        num1Len = len(num1)
        num2Len = len(num2)
        carry = '0'
        ans = ''
        for i in range(num1Len):
            if i > num2Len - 1:
                num2Number = 0
            else:
                num2Number = int(num2[num2Len - i - 1])

            temp = str(int(num1[num1Len - i - 1]) + num2Number + int(carry))
            carry = '0'
            if len(temp) > 1:
                carry = temp[0]
                ans = temp[1] + ans
            else:
                ans = temp[0] + ans
        if carry != '0':
            ans = carry + ans

        return ans
