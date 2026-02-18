# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0
        self.dfs(root, -200)
        return self.goodCount

    def dfs(self, node: TreeNode, prevMax: int) -> None:
        if prevMax <= node.val:
            prevMax = node.val
            self.goodCount = self.goodCount + 1

        if node.left:
            self.dfs(node.left, prevMax)

        if node.right:
            self.dfs(node.right, prevMax)
