
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
// User function Template for C++
class Solution {
  public:
    int numberOfEnclaves(vector<vector<int>> &grid) {
        // Code here
        queue<pair<int,int>> q;
        int n=grid.size();
        int m=grid[0].size();
        int vis[n][m] ={0};
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(i==0 || j==0 || i==n-1 || j==m-1){
                    if(grid[i][j]==1){
                        q.push({i,j});
                        vis[i][j]=1;
                    }
                }
            }
        }
        int delrow[] ={-1,0,+1,0};
        int delcol[] ={0,-1,0,+1};
        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();
            for(int i=0;i<4;i++){
                int nrow=row+delrow[i];
                int ncol=col+delcol[i];
                if(nrow>=0 && ncol>=0 && nrow<n && ncol<m &&
                    vis[nrow][ncol]==0 && grid[nrow][ncol]==1){
                        q.push({nrow,ncol});
                        vis[nrow][ncol]=1;
                }
            }
        }
        int cnt =0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1 && vis[i][j]==0){
                    cnt++;
                }
            }
        }
        return cnt;
        
    }
};
int main() {
    // Example usage
    Solution sol;
    vector<vector<int>> grid = {
        {0, 0, 1, 0},
        {1, 1, 0, 1},
        {0, 1, 1, 0},
        {0, 0, 0, 0}
    };
    int result = sol.numberOfEnclaves(grid);
    
    // Output the result
    cout << result << endl; // Expected output: number of enclaves
    return 0;
}