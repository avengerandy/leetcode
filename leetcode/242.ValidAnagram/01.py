class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = dict()
        for i in s:
            counter[i] = 1 + counter.get(i, 0)

        for i in t:
            counter[i] = counter.get(i, 0) - 1

        for key, value in counter.items():
            if value != 0:
                return False

        return True
