# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        levelans = []
        levelLen = 1
        queue = [root]
        while len(queue) != 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                levelans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(levelans)
            levelans = []

        if len(levelans) != 0:
            ans.append(levelans)
        return ans
