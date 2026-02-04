# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        self.counter = 0
        self.k = k
        self.dfs(root)
        return self.ans

    def dfs(self, root: Optional[TreeNode]) -> None:
        if root.left is not None:
            self.dfs(root.left)

        self.counter = self.counter + 1
        if self.counter == self.k:
            self.ans = root.val
            return

        if root.right is not None:
            self.dfs(root.right)
