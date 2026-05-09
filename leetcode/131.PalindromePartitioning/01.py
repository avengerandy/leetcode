class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.tempAns = []
        self.ans = []
        self.dfs(0)

        return self.ans

    def dfs(self, l):
        if l == len(self.s):
            self.ans.append(self.tempAns.copy())

        for r in range(l, len(self.s)):
            if self.isPalindrome(l, r):
                self.tempAns.append(self.s[l:r + 1])
                self.dfs(r + 1)
                self.tempAns.pop()

    def isPalindrome(self, l, r):
        while l < r:
            if self.s[l] != self.s[r]:
                return False
            l = l + 1
            r = r - 1
        return True
