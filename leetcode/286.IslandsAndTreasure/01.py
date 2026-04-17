class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        step = 0
        visited = set()
        while len(queue):
            newQueue = []
            for idx in range(len(queue)):
                location = queue[idx]
                if location[0] < 0 or location[1] < 0:
                    continue
                if location[0] > len(grid) - 1 or location[1] > len(grid[0]) - 1:
                    continue
                if location in visited:
                    continue
                if grid[location[0]][location[1]] == -1:
                    continue

                visited.add(location)
                grid[location[0]][location[1]] = step

                newQueue.append((location[0] - 1, location[1]))
                newQueue.append((location[0] + 1, location[1]))
                newQueue.append((location[0], location[1] - 1))
                newQueue.append((location[0], location[1] + 1))
            step = step + 1
            queue = newQueue
