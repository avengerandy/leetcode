import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))

        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_time > distances[curr_node]:
                continue

            for neighbor, travel_time in adj[curr_node]:
                new_time = curr_time + travel_time
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        max_time = max(distances.values())
        return max_time if max_time != float('inf') else -1
