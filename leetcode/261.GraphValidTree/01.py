class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.n = n
        self.visit = [False] * n
        self.edges = set()
        for edge in edges:
            self.edges.add((edge[0], edge[1]))
            self.edges.add((edge[1], edge[0]))

        notCircle = self.dfs(0)
        allVisit = sum(self.visit) == n

        return notCircle and allVisit

    def dfs(self, node: int) -> bool:
        if self.visit[node]:
            return False
        self.visit[node] = True

        for i in range(self.n):
            if (i, node) in self.edges or (node, i) in self.edges:
                self.edges.discard((i, node))
                self.edges.discard((node, i))
                if not self.dfs(i):
                    return False
        return True
