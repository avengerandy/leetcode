# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.dfs(root, 0)
        return self.depth

    def dfs(self, node: Optional[TreeNode], depth) -> int:
        if not node:
            return

        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
        self.depth = max(self.depth, depth + 1)
