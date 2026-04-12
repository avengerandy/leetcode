"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        self.visited = {}
        return self.dfs(node)

    def dfs(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.visited:
            return self.visited[node]
        copy = Node(node.val)
        self.visited[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor))
        return copy
