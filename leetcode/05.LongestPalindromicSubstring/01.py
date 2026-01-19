class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            if i == 0:
                longest = s[i]
                continue

            if s[i] == s[i-1]:
                left = i-1
                right = i
                while True:
                    if right == len(s) - 1:
                        break
                    if left == 0:
                        break
                    if s[left - 1] == s[right + 1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break

                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

            if i != len(s) - 1 and  s[i+1] == s[i-1]:
                left = i-1
                right = i+1
                while s[left] == s[right]:
                    if right == len(s) - 1:
                        break
                    if left == 0:
                        break
                    if s[left - 1] == s[right + 1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break

                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

        return longest
