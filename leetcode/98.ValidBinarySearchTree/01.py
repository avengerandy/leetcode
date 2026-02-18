# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -1001, 1001)

    def dfs(self, node: Optional[TreeNode], mimimum: int, maximum: int) -> bool:
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False

        if node.right and node.right.val >= maximum:
            return False

        if node.left and node.left.val <= mimimum:
            return False

        if node.left:
            if not self.dfs(node.left, mimimum, node.val):
                return False
        if node.right:
            if not self.dfs(node.right, node.val, maximum):
                return False

        return True
