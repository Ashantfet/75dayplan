// User function Template for C++

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include<set>
using namespace std;
class Solution {
  private:
    bool dfscheck(int node,vector<int> adj[],int vis[],int pathVis[],int check[]){
        vis[node]=1;
        pathVis[node]=1;
        check[node]=0;
        for(auto it :adj[node]){
            if(!vis[it]){
                if(dfscheck(it,adj,vis,pathVis,check)==true) return true;
            }
            else if(pathVis[it]) return true;
            
        }
        check[node]=1;
        pathVis[node]=0;
        return false;
    }
  public:
    vector<int> eventualSafeNodes(int V, vector<int> adj[]) {
        // code here
        int vis[V]={0};
        int pathVis[V]={0};
        int check[V]={0};
        vector<int> safeNodes;
        for(int i=0;i<V;i++){
            if(!vis[i]){
                dfscheck(i,adj,vis,pathVis,check);
            }
        }
        for(int i=0;i<V;i++){
            if(check[i]==1){
                safeNodes.push_back(i);
            }
        }
        return safeNodes;
    }
};

int main() {
    // Example usage
    Solution sol;
    int V = 5; // Number of vertices
    vector<int> adj[V];
    adj[0] = {1, 2};
    adj[1] = {2, 3};
    adj[2] = {3, 4};
    adj[3] = {};
    adj[4] = {};
    
    vector<int> result = sol.eventualSafeNodes(V, adj);
    
    // Output the result
    for(int node : result) {
        cout << node << " ";
    }
    return 0;
}
