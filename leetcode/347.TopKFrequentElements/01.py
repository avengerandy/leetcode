from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = defaultdict(int)
        for num in nums:
            cache[num] = cache[num] + 1

        heap = []
        for key, value in cache.items():
            heap.append((value, key))
        heapq.heapify_max(heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop_max(heap)[1])
        return ans
