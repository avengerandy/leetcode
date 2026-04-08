class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            hasBit = (1 << i) & n
            if hasBit:
                ans += 1
        return ans
