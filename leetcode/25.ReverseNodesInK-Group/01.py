# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None
        groupHead = head
        while True:
            node = groupHead

            for i in range(k - 1):
                if node is None:
                    break
                node = node.next

            if node is not None:
                nextGroupHead = node.next
                node.next = None
                head, end = self.reverseListWithHeadAndEnd(groupHead)
            else:
                prevEnd.next = groupHead
                break

            if newHead is None:
                newHead = head
            else:
                prevEnd.next = head
            prevEnd = end
            groupHead = nextGroupHead

        return newHead

    def reverseListWithHeadAndEnd(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev, head
