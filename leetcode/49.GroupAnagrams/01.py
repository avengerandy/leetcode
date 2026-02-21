class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempCache = dict()
        for string in strs:
            encodeInt = 0
            for char in string:
                index = ord(char) - 97
                encodeInt = encodeInt + pow(10, index)
            if encodeInt in tempCache:
                tempCache[encodeInt].append(string)
            else:
                tempCache[encodeInt] = [string]
        ans = []
        for key, value in tempCache.items():
            ans.append(value)
        return ans
