/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr) return nullptr;
        queue<Node* > q;
        map<Node*, Node*> clones;
        clones[node] = new Node(node->val);
        q.push(node);
        while(!q.empty()){
            Node* current = q.front();
            q.pop();
            for(auto neighbor : current->neighbors){
                if(clones.find(neighbor) == clones.end()){
                    clones[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                clones[current]->neighbors.push_back(clones[neighbor]);
            }
        }
        return clones[node];
        
    }
};