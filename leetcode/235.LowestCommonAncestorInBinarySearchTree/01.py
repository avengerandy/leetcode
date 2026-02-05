# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        while (p.val < lca.val and q.val < lca.val) or (p.val > lca.val and q.val > lca.val):
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left
            if p.val > lca.val and q.val > lca.val:
                lca = lca.right
        return lca
