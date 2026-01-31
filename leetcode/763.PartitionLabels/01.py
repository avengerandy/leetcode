class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervalCache = dict()
        for i in range(len(s)):
            char = s[i]
            if char not in intervalCache:
                intervalCache[char] = [i, i]
            else:
                intervalCache[char][1] = i

        substringLens = []
        endIdx = 0
        startIdx = 0
        for key, interval in intervalCache.items():
            if interval[0] > endIdx:
                substringLen = endIdx - startIdx + 1
                substringLens.append(substringLen)
                startIdx = interval[0]
                endIdx = interval[1]
            else:
                endIdx = max(interval[1], endIdx)
        substringLen = endIdx - startIdx + 1
        substringLens.append(substringLen)
        return substringLens
