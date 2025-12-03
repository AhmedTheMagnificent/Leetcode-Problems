#include <unordered_set>
#include <stack>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class FindElements {
private:
    unordered_set<int> values; // store all recovered node values
public:
    FindElements(TreeNode* root) {
        if (!root) return;
        root->val = 0;
        stack<TreeNode*> st;
        st.push(root);
        
        while (!st.empty()) {
            TreeNode* node = st.top(); st.pop();
            values.insert(node->val);
            
            if (node->left) {
                node->left->val = 2 * node->val + 1;
                st.push(node->left);
            }
            if (node->right) {
                node->right->val = 2 * node->val + 2;
                st.push(node->right);
            }
        }
    }
    
    bool find(int target) {
        return values.count(target) > 0;
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
