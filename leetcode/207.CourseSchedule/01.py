class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjacencyList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for prerequisite in prerequisites:
            adjacencyList[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] = indegree[prerequisite[0]] + 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while len(queue):
            i = queue.popleft()
            for neighbor in adjacencyList[i]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return not sum(indegree)
