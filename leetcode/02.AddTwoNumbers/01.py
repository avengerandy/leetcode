# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        root = l1
        ans = l1.val + l2.val
        l1.val = ans % 10
        carry = ans // 10
        while l1.next is not None or l2.next is not None:
            if l1.next is None:
                l1.next = ListNode()
            if l2.next is None:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next

            ans = l1.val + l2.val + carry
            l1.val = ans % 10
            carry = ans // 10

        if carry > 0:
            l1.next = ListNode(carry)

        return root
