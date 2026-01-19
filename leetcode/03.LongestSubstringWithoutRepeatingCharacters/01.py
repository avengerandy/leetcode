class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        for i in s:
            cache[i] = False

        longest = 0
        long = 0
        pointer = 0
        for idx, i in enumerate(s):
            if cache[i] == False:
                cache[i] = True
                long = long + 1
                longest = max(longest, long)
            else:
                while s[pointer] != i:
                    cache[s[pointer]] = False
                    pointer = pointer + 1
                long = idx - pointer
                pointer = pointer + 1

        return longest
