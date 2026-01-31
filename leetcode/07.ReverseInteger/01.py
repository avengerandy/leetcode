class Solution:
    def reverse(self, x: int) -> int:
        max32Int = 2147483648 # 2^31
        print(max32Int)
        ans = int(str(abs(x))[::-1])
        if x > 0:
            if ans > max32Int - 1:
                return 0
            return ans
        if ans > max32Int:
            return 0
        return -ans
