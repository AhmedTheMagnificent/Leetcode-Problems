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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* merged = nullptr;
        ListNode* nodeptr = nullptr;
        while(list1 && list2){
            ListNode* newnode = new ListNode();
            if(list1->val <= list2->val){
                newnode->val = list1->val;
                list1 = list1->next;
            }
            else{
                newnode->val = list2->val;
                list2 = list2->next;
            }
            if(!merged){
                merged = newnode;
                nodeptr = merged;
            }
            else{
                nodeptr->next = newnode;
                nodeptr = nodeptr->next;
            }
        }
        if(list1){
            if(!merged){
                merged = list1;
            }
            else{
                nodeptr->next = list1;
            }
        }
        if(list2){
            if(!merged){
                merged = list2;
            }
            else{
                nodeptr->next = list2;
            }
        }
        return merged;
    }
};