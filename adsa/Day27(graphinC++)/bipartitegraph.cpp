

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include<set>
using namespace std;
class Solution {
  private:
    bool check(int start, int V,vector<vector<int>> &adj,vector<int>  &color){
        queue<int> q;
        q.push(start);
        color[start]=0;
        while(!q.empty()){
            int node=q.front();
            q.pop();
            for(auto it: adj[node]){
                if(color[it]==-1){
                    color[it]=!color[node];
                    q.push(it);
                }
                else if(color[it]==color[node]){
                    return false;
                }
            }
        }
        return true;
    }
  public:
    bool isBipartite(int V, vector<vector<int>> &edges) {
        // Code here
        vector<vector<int>> adj(V);
        int n= edges.size();
        for(int i=0;i<n;i++){
            int u=edges[i][0];
            int v=edges[i][1];
            adj[v].push_back(u);
            adj[u].push_back(v);
        }
        vector<int> color(V, -1);
        for(int i=0;i<V;i++){
            if(color[i]==-1){
                if(check(i,V,adj,color)==false){
                    return false;
                }
            }
        }
        return true;
    }
};
int main() {
    // Example usage
    Solution sol;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 0}}; // Example bipartite graph
    int V = 5; // Number of vertices
    bool result = sol.isBipartite(V, edges);
    
    // Output the result
    cout << (result ) << endl;
    return 0;
}