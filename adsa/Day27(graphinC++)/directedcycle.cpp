#include <iostream>
#include <vector>
#include <stack>
using namespace std;
class Solution {
  private:
    bool dfscheck(int node,vector<vector<int>> &adj,int vis[],int pathVis[]){
        vis[node]=1;
        pathVis[node]=1;
        for(auto it :adj[node]){
            if(!vis[it]){
                if(dfscheck(it,adj,vis,pathVis)==true) return true;
            }
            else if(pathVis[it]) return true;
            
        }
        pathVis[node]=0;
        return false;
    }
  public:
    bool isCyclic(int V, vector<vector<int>> &edges) {
        // code here
        vector<vector<int>> adj(V);
        int n= edges.size();
        for(int i=0;i<n;i++){
            int u=edges[i][0];
            int v=edges[i][1];
            //adj[v].push_back(u);
            adj[u].push_back(v);
        }
        int vis[V]={0};
        int pathVis[V]={0};
        for(int i=0;i<V;i++){
            if(!vis[i]){
                if(dfscheck(i,adj,vis,pathVis)==true){
                    return true;
                }
            }
        }
        return false;
    }
};

int main() {
    // Example usage
    Solution sol;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}}; // Example directed graph with a cycle
    int V = 3; // Number of vertices
    bool result = sol.isCyclic(V, edges);
    
    // Output the result
    cout << (result ) << endl;
    return 0;
}