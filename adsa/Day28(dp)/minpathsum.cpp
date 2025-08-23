#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int i,int j,vector<vector<int>>& grid,vector<vector<int>>& dp){   //dp method
//         if(i==0 && j==0) return grid[0][0];
//         if(i<0 || j<0) return 1e9;
//         if (dp[i][j]!=-1) return dp[i][j];
        
//         int up=grid[i][j] +fun(i-1,j,grid,dp);
//         int left=grid[i][j] +fun(i,j-1,grid,dp);
//         return dp[i][j]=min( up, left);
//     }
// public:
//     int minPathSum(vector<vector<int>>& grid) {
//         int m=grid.size();
//         int n=grid[0].size();
//         vector<vector<int>> dp(m,vector<int>(n,0));
//         for(int i=0;i<m;i++){
//             for(int j=0;j<n;j++){
//                 if(i==0 && j==0) dp[0][0]=grid[0][0];
//                 else {
//                     int up=grid[i][j];
//                     if(i>0) up+=dp[i-1][j];
//                     else up+=1e9;
//                     int left=grid[i][j];
//                     if(j>0) left+=dp[i][j-1];
//                     else left+=1e9;
//                     dp[i][j]=min(up,left);
//                 }

//             }
//         }
//         return dp[m-1][n-1];

//         //return fun(m-1,n-1,grid,dp);
//     }
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        vector<int> prev(n,0);
        for(int i=0;i<m;i++){
            vector<int> cur(n,0);
            for(int j=0;j<n;j++){
                if(i==0 && j==0) cur[0]=grid[0][0];
                else {
                    int up=grid[i][j];
                    if(i>0) up+=prev[j];
                    else up+=1e9;
                    int left=grid[i][j];
                    if(j>0) left+=cur[j-1];
                    else left+=1e9;
                    cur[j]=min(up,left);
                }
                
            }
            prev.swap(cur);

        }
        return prev[n-1];

        //return fun(m-1,n-1,grid,dp);
    }
};

int main() {
    // Example usage
    Solution sol;
    vector<vector<int>> grid = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };
    int result = sol.minPathSum(grid);
    
    // Output the result
    cout << result << endl; // Output: 7
    return 0;
}