from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjacencyList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for prerequisite in prerequisites:
            adjacencyList[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] = indegree[prerequisite[0]] + 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        while len(queue):
            i = queue.popleft()
            ans.append(i)
            for neighbor in adjacencyList[i]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [] if sum(indegree) else ans
