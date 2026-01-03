# Multi-digit multiplication using multiplication as the primitive operation;
# if necessary, faster algorithms like Karatsuba or FFT can be considered.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1Len = len(num1)
        num2Len = len(num2)
        ans = [0] * (num1Len + num2Len)
        for i in range(num1Len):
            for j in range(num2Len):
                index1 = num1Len - i - 1
                index2 = num2Len - j - 1
                num1Number = int(num1[index1])
                num2Number = int(num2[index2])
                temp = num1Number * num2Number + ans[index1 + index2 + 1]
                ans[index1 + index2] = ans[index1 + index2] + temp // 10 # carry
                ans[index1 + index2 + 1] = temp % 10

        if ans[0] == 0:
            ans.pop(0)
        ans = map(str, ans)
        return ''.join(ans)
