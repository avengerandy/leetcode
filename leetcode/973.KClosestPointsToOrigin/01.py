import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([(x ** 2) + (y ** 2), x, y])

        minK = heapq.nsmallest(k, distances)

        ans = []
        for distance, x, y in minK:
            ans.append([x, y])
        return ans
