import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        heapq.heappush(self.large, heapq.heappop_max(self.small))

        if len(self.small) < len(self.large):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2
        return self.small[0]
