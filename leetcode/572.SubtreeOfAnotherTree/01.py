# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRoot = subRoot
        return self.dfs(root)

    def dfs(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return False

        if self.isSameTree(node, self.subRoot):
            return True

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        return left or right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) ^ (q is None):
            return False
        if p is None:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
