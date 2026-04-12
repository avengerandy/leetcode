# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root, 0)
        return self.diameter - 1

    def dfs(self, node: Optional[TreeNode], depth) -> int:
        if not node:
            return depth

        leftDepth = self.dfs(node.left, depth + 1) - depth - 1
        rightDepth = self.dfs(node.right, depth + 1) - depth - 1
        self.diameter = max(self.diameter, leftDepth + rightDepth + 1)

        return max(leftDepth, rightDepth) + depth + 1
