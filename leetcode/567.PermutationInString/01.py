class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = {}
        s2Map = {}
        for idx, char in enumerate(s1):
            if s1Map.get(char) is not None:
                s1Map[char] = s1Map[char] + 1
            else:
                s1Map[char] = 1

            if s2Map.get(char) is None:
                s2Map[char] = 0
            if s2Map.get(s2[idx]) is not None:
                s2Map[s2[idx]] = s2Map[s2[idx]] + 1
            else:
                s2Map[s2[idx]] = 1
        same = True
        for k in s1Map.keys():
            if s1Map[k] != s2Map[k]:
                same = False
        if same:
            return True

        totalLen = len(s1)
        for i in range(totalLen, len(s2)):
            # front
            if s2Map.get(s2[i]) is not None:
                s2Map[s2[i]] = s2Map[s2[i]] + 1
            else:
                s2Map[s2[i]] = 1
            # back
            s2Map[s2[i-totalLen]] = s2Map[s2[i-totalLen]] - 1

            same = True
            for k in s1Map.keys():
                if s1Map[k] != s2Map[k]:
                    same = False
            if same:
                return True
        return False
