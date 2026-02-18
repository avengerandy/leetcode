class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])
        ans = []
        for i in range(len(intervals)):
            if i != 0 and intervals[i][0] <= ans[-1][1]:
                ans[-1][0] = min(intervals[i][0], ans[-1][0])
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
                continue
            ans.append(intervals[i])

        return ans
