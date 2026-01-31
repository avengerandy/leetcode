# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        emptyStart = ListNode()
        emptyStart.next = head

        listLen = 0
        node = emptyStart
        while node:
            node = node.next
            listLen = listLen + 1

        target = listLen - n - 1
        node = emptyStart
        for i in range(target):
            node = node.next
        if node.next:
            node.next = node.next.next

        return emptyStart.next
