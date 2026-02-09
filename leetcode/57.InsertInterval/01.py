class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        flag = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ans.append(interval)
                continue
            if interval[0] > newInterval[1]:
                if not flag:
                    ans.append(newInterval)
                    flag = True
                ans.append(interval)
                continue
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
        if not flag:
            ans.append(newInterval)
        return ans
