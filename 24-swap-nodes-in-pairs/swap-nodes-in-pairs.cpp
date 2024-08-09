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
    ListNode* swapPairs(ListNode* head) {
        if(!head){
            return nullptr;
        }
        else if(head && !head->next){
            return head;
        }
        else{
            ListNode *i = head;
            head = head->next;
            ListNode *j = head;
            ListNode *nodeptr = nullptr;
            while(i && j){
                nodeptr = i;
                i->next = j->next;
                j->next = i;
                i = i->next;
                if(!i){
                    j = nullptr;
                }
                else{
                    j = i->next;
                }
                if(j){
                    nodeptr->next = j;
                }
            }
            return head;
        }
    }
};