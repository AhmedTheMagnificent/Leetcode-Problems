class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> nodes;
        vector<bool> visited(n, false);
        for(auto &edge : edges){
            visited[edge[1]] = true; 
        }
        for(int i = 0; i < visited.size(); i++){
            if(!visited[i]){
                nodes.push_back(i);
            }
        }
        return nodes;
    }
};