/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || k == 0) {
            return head;
        }

        int total = 1;
        ListNode* last = head;
        while (last->next != nullptr) {
            total = total + 1;
            last = last->next;
        }

        int breakNodeIndex = total - (k % total);
        if (breakNodeIndex == total) {
            return head;
        }

        last->next = head;
        ListNode* newHead = nullptr;

        int currentIndex = 1;
        while (head->next != nullptr) {
            if (currentIndex == breakNodeIndex) {
                newHead = head->next;
                head->next = nullptr;
                return newHead;
            }
            head = head->next;
            currentIndex = currentIndex + 1;
        }
        return newHead;
    }
};
