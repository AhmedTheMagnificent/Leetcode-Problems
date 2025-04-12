class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path;
        vector<vector<int>> result;
        dfs(0, graph, path, result);
        return result;

    }
    void dfs(int node, vector<vector<int>> &graph, vector<int> &path, vector<vector<int>> &result){
        path.push_back(node);
        if(node == graph.size() - 1) result.push_back(path);
        else{
            for(auto neighbour : graph[node]){
                dfs(neighbour, graph, path, result);
            }
        }
        path.pop_back();
    }
};