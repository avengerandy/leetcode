# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        node = head
        memery = []
        while node is not None:
            memery.append(node)
            node = node.next

        left = 0
        right = len(memery) - 1
        node = ListNode()
        while left < right:
            node.next = memery[left]
            node = node.next

            node.next = memery[right]
            node = node.next

            left = left + 1
            right = right - 1

        if left == right:
            node.next = memery[left]
            node = node.next
        node.next = None
