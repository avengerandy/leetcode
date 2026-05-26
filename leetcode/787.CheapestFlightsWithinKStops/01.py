class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.k = k
        self.adj = dict()
        self.ans = float('inf')
        self.visited = set()
        self.dst = dst

        for i in range(n):
            self.adj[i] = dict()
        for flight in flights:
            self.adj[flight[0]][flight[1]] = flight[2]

        self.dfs(src, -1, 0)
        return self.ans if self.ans != float('inf') else -1

    def dfs(self, flightIdx: int, step: int, priceSum: int) -> None:
        if flightIdx in self.visited:
            return
        self.visited.add(flightIdx)

        if priceSum > self.ans:
            self.visited.remove(flightIdx)
            return

        if step > self.k:
            self.visited.remove(flightIdx)
            return

        if flightIdx == self.dst:
            self.visited.remove(flightIdx)
            self.ans = min(priceSum, self.ans)
            return

        for neighborIdx, price in self.adj[flightIdx].items():
            self.dfs(neighborIdx, step + 1, priceSum + price)
        self.visited.remove(flightIdx)
