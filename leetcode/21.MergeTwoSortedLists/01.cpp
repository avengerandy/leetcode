/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(0);
        ListNode* ansHead = new ListNode(0);
        ansHead->next = ans;
        while(l1 != nullptr || l2 != nullptr) {
            if (l1 == nullptr) {
                ans->next = l2;
                l2 = l2->next;
            } else if (l2 == nullptr) {
                ans->next = l1;
                l1 = l1->next;
            } else if (l1->val > l2->val) {
                ans->next = l2;
                l2 = l2->next;
            } else {
                ans->next = l1;
                l1 = l1->next;
            }
            ans = ans->next;
        }
        return ansHead->next->next;
    }
};