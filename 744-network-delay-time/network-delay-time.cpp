class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // making graph
        vector<vector<pair<int, int>>> graph(n + 1);
        for(auto time: times){
            int u = time[0], v = time[1], w = time[2];
            graph[u].push_back({v, w});
        }

        vector<int> dist (n + 1, INT_MAX);
        dist[k] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, k});
        while(!pq.empty()){
            auto [currDistance, u] = pq.top(); pq.pop();
            if(dist[u] < currDistance) continue;
            
            for(auto [v, w] : graph[u]){
                if(dist[u] + w < dist[v]){
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }}
            int maxTime = 0;
            for(int i = 1; i <= n; i++){
                if(dist[i] == INT_MAX) return -1;
                maxTime = max(maxTime, dist[i]);
            }
            
        
        return maxTime;
    }
};