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
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // min-heap
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int length = lists.size();
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;
        for(auto node : lists){
            if (node != nullptr) {
                minHeap.push(node);
            }      
        }
        ListNode head;
        ListNode* tail = &head;

        while(!minHeap.empty()){
            ListNode* smallest = minHeap.top();
            minHeap.pop();
            tail->next = smallest;
            tail = tail->next;
            if(smallest->next){
                minHeap.push(smallest->next);
            }
        }

        return head.next;
    }
};