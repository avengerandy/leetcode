class Solution:
    def countSubstrings(self, s: str) -> int:
        self.counter = 0
        self.s = s
        for i in range(len(s)):
            self.countPalindrome(i, i)
            self.countPalindrome(i, i + 1)
        return self.counter

    def countPalindrome(self, l: int, r: int) -> None:
        while l >= 0 and r < len(self.s):
            if self.s[l] != self.s[r]:
                return
            l = l - 1
            r = r + 1
            self.counter = self.counter + 1
