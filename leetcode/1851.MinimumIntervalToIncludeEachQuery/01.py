class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        pointer = 0
        for query in sorted(queries):
            while pointer < len(intervals) and intervals[pointer][0] <= query:
                start, end = intervals[pointer]
                heapq.heappush(minHeap, (end - start + 1, end))
                pointer += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            res[query] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
