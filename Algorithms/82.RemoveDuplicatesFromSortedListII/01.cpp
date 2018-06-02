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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return nullptr;
        ListNode* temp = head;
        ListNode* duplicates = head;
        bool duplicatesFlag = false;
        
        while(temp->next != nullptr) {
            if (temp->val == temp->next->val) {
                duplicatesFlag = true;
                temp = temp->next;
                continue;
            }
            if(duplicatesFlag) {
                if (duplicates == head && temp->val == head->val) return deleteDuplicates(temp->next);
                duplicates->next = temp->next;
                temp = temp->next;
                duplicatesFlag = false;
                continue;
            }
            duplicates = temp;
            temp = temp->next;
        }
        
        if(duplicatesFlag) {
            if (duplicates == head && temp->val == head->val) return nullptr;
            duplicates->next = nullptr;
        }
        return head;
    }
};