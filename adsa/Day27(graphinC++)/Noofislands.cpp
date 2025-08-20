#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
class Solution {
private:
    void bfs(int row,int col,vector<vector<int>> &vis,vector<vector<char>> &grid){
        vis[row][col] =1;
        queue<pair<int,int>> q;
        q.push({row,col});
        int n=grid.size();
        int m=grid[0].size();
        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop();
            int dr[4] = {-1, 0, 1, 0};
            int dc[4] = {0, 1, 0, -1};
            for (int i = 0; i < 4; i++) {
                int nrow = r + dr[i];
                int ncol = c + dc[i];

                if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
                    grid[nrow][ncol] == '1' && !vis[nrow][ncol]) {
                    vis[nrow][ncol] = 1;
                    q.push({nrow, ncol});
                }
                
            }

        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int n=grid.size();
        int m= grid[0].size();
        vector<vector<int>> vis(n,vector<int>(m,0));
        int cnt =0;
        for (int row =0;row<n;row++){
            for(int col=0;col<m;col++){
                if (!vis[row][col] && grid[row][col]=='1'){
                    cnt++;
                    bfs(row,col,vis,grid);
                }
            }
        }
        return cnt;
    }
};

int main() {
    // Example usage
    Solution sol;
    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '1', '1'},
        {'0', '0', '0', '0', '0'},
        {'0', '1', '1', '0', '0'}
    };
    int result = sol.numIslands(grid);
    
    // Output the result
    cout << result << endl; // Output: 3
    return 0;
}