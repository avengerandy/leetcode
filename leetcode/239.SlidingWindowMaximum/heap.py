import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))
        maxNumber = [heap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] <= (i - k):
                heapq.heappop_max(heap)
            maxNumber.append(heap[0][0])

        return maxNumber
