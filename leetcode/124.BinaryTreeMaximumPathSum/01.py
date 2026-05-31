# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = -1000000
        self.dfs(root)
        return self.maximum

    def dfs(self, node: TreeNode) -> int:
        leftValue = 0
        if node.left:
            leftValue = max(leftValue, self.dfs(node.left))
        rightValue = 0
        if node.right:
            rightValue = max(rightValue, self.dfs(node.right))

        maxSumOfNode = max(node.val, leftValue + rightValue + node.val)
        self.maximum = max(self.maximum, maxSumOfNode)
        return max(rightValue + node.val, leftValue + node.val)
