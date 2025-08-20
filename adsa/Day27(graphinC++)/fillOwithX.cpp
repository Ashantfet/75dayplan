// User function Template for C++
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
// User function Template for C++

class Solution {
  private:
    void dfs(int row,int col,vector<vector<int>> &vis,vector<vector<char>> &mat){
        vis[row][col]=1;
        int delrow[] ={-1,0,1,0};
        int delcol[] ={0,-1,0,1};
        int n=mat.size();
        int m=mat[0].size();
        for(int i=0;i<4;i++){
            int ncol=col+delcol[i];
            int nrow=row+delrow[i];
            if(nrow>=0 && ncol>=0 && nrow <n && ncol <m && !vis[nrow][ncol] && mat[nrow][ncol]=='O'){
                dfs(nrow,ncol,vis,mat);
            }
        }
    }
  public:
    vector<vector<char>> fill(vector<vector<char>>& mat) {
        // code here
        int n=mat.size();
        int m=mat[0].size();
        vector<vector<int>> vis(n,vector<int>(m,0));
        for(int j=0;j<m;j++){
            if(!vis[0][j] && mat[0][j] =='O'){
                dfs(0,j,vis,mat);
            }
            if(!vis[n-1][j] && mat[n-1][j] =='O'){
                dfs(n-1,j,vis,mat);
            }
        }
        for(int j=0;j<n;j++){
            if(!vis[j][0] && mat[j][0] =='O'){
                dfs(j,0,vis,mat);
            }
            if(!vis[j][m-1] && mat[j][m-1] =='O'){
                dfs(j,m-1,vis,mat);
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!vis[i][j] && mat[i][j]=='O'){
                    mat[i][j]='X';
                }
            }
        }
        return mat;
    }
};
int main() {
    // Example usage
    Solution sol;
    vector<vector<char>> mat = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}
    };
    vector<vector<char>> result = sol.fill(mat);
    
    // Output the result
    for (const auto& row : result) {
        for (char val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}
