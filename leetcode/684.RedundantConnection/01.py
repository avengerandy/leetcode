class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(i):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False

            parent[root_i] = root_j
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
