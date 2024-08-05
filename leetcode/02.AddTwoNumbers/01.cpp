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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ansListNode = new ListNode(0);
        ListNode* ansListNodeHead = ansListNode;

        int carry = 0;
        while (l1 != nullptr || l2 != nullptr) {
            int a = l1 ? l1->val : 0;
            int b = l2 ? l2->val : 0;
            int sum = a + b + carry;
            carry = sum / 10;
            ListNode* nextListNode = new ListNode(sum%10);
            ansListNode->next = nextListNode;
            ansListNode = ansListNode->next;
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        if (carry > 0) {
            ansListNode->next = new ListNode(carry);
        }
        return ansListNodeHead->next;
    }
};