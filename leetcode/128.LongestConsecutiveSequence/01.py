class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set()
        ans = 0

        for i in nums:
            cache.add(i)

        for i in nums:
            if i - 1 in cache:
                continue
            tempCounter = 1
            while i + tempCounter in cache:
                tempCounter = tempCounter + 1
            ans = max(ans, tempCounter)

        return ans
