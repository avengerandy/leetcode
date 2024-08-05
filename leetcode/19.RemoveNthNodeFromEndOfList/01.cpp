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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        vector<ListNode*> elements;
        int size = 0;
        while(temp != nullptr) {
            elements.push_back(temp);
            temp = temp->next;
            size++;
        }
        if (n == size) {
            return head->next;
        }
        if (n == 1) {
            elements[size-2]->next = nullptr;
            return head;
        }
        elements[size-1-n]->next = elements[size-n+1];
        return head;
    }
};