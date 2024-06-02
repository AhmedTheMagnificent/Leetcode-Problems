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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *l, *r;
        r = head;
        l = head;
        while(r != nullptr){
            if(r->val == l->val && r != l){
                l->next = r->next;
                r = l->next;
            }
            else{
                l = r;
                r = l->next;
            }
        }
        return head;
    }
};