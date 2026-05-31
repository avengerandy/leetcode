# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        if root:
            self.dfs(0, root)
        return self.ans

    def dfs(self, deep: int, node: Optional[TreeNode]) -> None:
        if len(self.ans) < deep + 1:
            self.ans.append(node.val)
        else:
            self.ans[deep] = node.val
        if node.left:
            self.dfs(deep + 1, node.left)
        if node.right:
            self.dfs(deep + 1, node.right)
