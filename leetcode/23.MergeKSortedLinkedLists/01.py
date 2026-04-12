# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        start = lists[0]
        for idx in range(1, len(lists)):
            start = self.merge(start, lists[idx])

        return start

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:

        ans = ListNode()
        ansHead = ListNode()
        ansHead.next = ans

        while l1 != None or l2 != None:
            if l1 == None:
                ans.next = l2
                l2 = l2.next
            elif l2 == None:
                ans.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                ans.next = l2
                l2 = l2.next
            else:
                ans.next = l1
                l1 = l1.next
            ans = ans.next

        return ansHead.next.next;
