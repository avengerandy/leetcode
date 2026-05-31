# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        strTree = []
        queue = deque([root])
        while len(queue):
            node = queue.popleft()
            if node is None:
                strTree.append(node)
            else:
                strTree.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(str(s) for s in strTree)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        strTree = data.split(',')
        if strTree[0] == 'None':
            return None
        root = TreeNode(int(strTree[0]))
        queue = deque([root])
        counter = 1
        while queue:
            node = queue.popleft()
            if strTree[counter] != 'None':
                node.left = TreeNode(int(strTree[counter]))
                queue.append(node.left)
            counter = counter + 1
            if strTree[counter] != 'None':
                node.right = TreeNode(int(strTree[counter]))
                queue.append(node.right)
            counter = counter + 1
        return root
