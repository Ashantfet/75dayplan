#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
  private:
    void dfs(int node, int vis[], stack<int> &st, vector<int> adj[]) {
        vis[node]=1;
        for(auto it:adj[node]){
            if(!vis[it]){
                dfs(it,vis,st,adj);
            }
        }
        st.push(node);
    }
  public:
    vector<int> topoSort(int V, vector<vector<int>>& edges) {
        // code here
        vector<int> adj[V];
        int n= edges.size();
        for(int i=0;i<n;i++){
            int u=edges[i][0];
            int v=edges[i][1];
            //adj[v].push_back(u);
            adj[u].push_back(v);
        }
        int vis[V]={0};
        stack<int> st;
        for(int i=0;i<V; i++){
            if(!vis[i]){
                dfs(i,vis,st,adj);
            }
        }
        vector<int> ans;
        while(!st.empty()){
            ans.push_back(st.top());
            st.pop();
        }
        return ans;
    }
};

int main() {
    // Example usage
    Solution sol;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 3}, {3, 4}};
    int V = 5; // Number of vertices
    vector<int> result = sol.topoSort(V, edges);
    
    // Output the result
    for(int node : result) {
        cout << node << " ";
    }
    return 0;
}