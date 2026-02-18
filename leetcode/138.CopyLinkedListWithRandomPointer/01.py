"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.cache = dict()
        newList = Node(0)
        newHead = newList
        while head is not None:
            newList.next = self.getOrCreateNewNode(head)
            newList = newList.next
            head = head.next
        return newHead.next

    def getOrCreateNewNode(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if node is None:
            return node

        if node in self.cache:
            return self.cache[node]

        newNode = Node(node.val)
        self.cache[node] = newNode
        newNode.random = self.getOrCreateNewNode(node.random)
        return self.cache[node]
