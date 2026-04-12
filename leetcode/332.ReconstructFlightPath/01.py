from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adjList = defaultdict(list)
        for src, dst in tickets:
            # lexical order
            heapq.heappush(self.adjList[src], dst)
        self.ans = []
        self.dfs('JFK')
        return self.ans[::-1]

    def dfs(self, airport: str):
        destinations = self.adjList[airport]
        while destinations:
            # smallest lexical
            destination = heapq.heappop(destinations)
            self.dfs(destination)
        self.ans.append(airport)
