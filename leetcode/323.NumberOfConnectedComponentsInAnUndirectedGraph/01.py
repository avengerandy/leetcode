class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.edgesMap = [[] for _ in range(n)]
        self.visitMap = [False] * n

        for i, j in edges:
            self.edgesMap[i].append(j)
            self.edgesMap[j].append(i)

        counter = 0
        for node in range(n):
            if not self.visitMap[node]:
                self.visitMap[node] = True
                self.dfs(node)
                counter = counter + 1

        return counter

    def dfs(self, node):
        for connectNode in self.edgesMap[node]:
            if not self.visitMap[connectNode]:
                self.visitMap[connectNode] = True
                self.dfs(connectNode)
