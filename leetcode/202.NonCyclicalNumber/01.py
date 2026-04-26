class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()

        while n not in cache:
            cache.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True

        return False

    def sumOfSquares(self, number: int) -> int:
        ans = 0

        while number:
            digit = number % 10
            digit = digit ** 2
            ans = ans + digit
            number = number // 10

        return ans
