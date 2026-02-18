class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        powNumber = 1
        ans = x
        while powNumber * 2 <= abs(n):
            ans = ans * ans
            powNumber = powNumber * 2

        for i in range(abs(n) - powNumber):
            ans = ans * x

        if n < 0:
            ans = 1 / ans

        return ans
