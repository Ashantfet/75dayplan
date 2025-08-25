// User function Template for C++
#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int i,int j1,int j2,int m,int n,vector<vector<int>>& grid,vector<vector<vector<int>>>& dp){
//         if(j1<0 ||j2<0 || j1>=n||j2>=n) return -1e9;
//         if(i==m-1){
//             if(j1==j2) return grid[i][j1];
//             else return grid[i][j1]+grid[i][j2];
//         }
//         if(dp[i][j1][j2]!=-1) return dp[i][j1][j2];
//         int maxi=-1e9;
//         for(int dj1 = -1;dj1 <= 1; dj1++){
//             for(int dj2 = -1;dj2 <= 1; dj2++){
//                 int value=0;
//                 if(j1==j2) value=grid[i][j1];
//                 else value=grid[i][j1]+grid[i][j2];
//                 value+=fun(i+1,j1+dj1,j2+dj2,m,n,grid,dp);
//                 maxi=max(maxi,value);
//             }
//         }
//         return dp[i][j1][j2]=maxi;
//     }
public:
    // int cherryPickup(vector<vector<int>>& grid) {
    //     int m=grid.size();
    //     int n=grid[0].size();
    //     //vector<vector<vector<int>>> dp(m,vector<vector<int>>(n,vector<int>(n,-1)));
    //     //return fun(0,0,n-1,m,n,grid,dp);
    //     vector<vector<vector<int>>> dp(m,vector<vector<int>>(n,vector<int>(n,0)));
    //     for(int j1=0; j1<n;j1++){
    //         for(int j2=0;j2<n;j2++){
    //             if(j1==j2) dp[m-1][j1][j2]=grid[m-1][j1];
    //             else dp[m-1][j1][j2]=grid[m-1][j1]+grid[m-1][j2];
    //         }
    //     }
    //     for(int i=m-2;i>=0;i--){
    //         for(int j1=0; j1<n;j1++){
    //             for(int j2=0;j2<n;j2++){
    //                  int maxi=-1e9;
    //                 for(int dj1 = -1;dj1 <= 1; dj1++){
    //                     for(int dj2 = -1;dj2 <= 1; dj2++){
    //                         int value=0;
    //                         if(j1==j2) value=grid[i][j1];
    //                         else value=grid[i][j1]+grid[i][j2];
    //                         if(j1+dj1>=0 && j1+dj1<n && j2+dj2>=0 && j2+dj2<n)
    //                             value+=dp[i+1][j1+dj1][j2+dj2];
    //                         else value+=-1e9;
    //                         maxi=max(maxi,value);
    //                     }
    //                 }
    //                 dp[i][j1][j2]=maxi;
    //             }
    //         }
            
    //     }
    //     return dp[0][0][n-1];
    // }
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> next(n, vector<int>(n, 0));
        vector<vector<int>> curr(n, vector<int>(n, 0));

        // Base case: last row
        for (int j1 = 0; j1 < n; j1++) {
            for (int j2 = 0; j2 < n; j2++) {
                if (j1 == j2) next[j1][j2] = grid[m - 1][j1];
                else next[j1][j2] = grid[m - 1][j1] + grid[m - 1][j2];
            }
        }

        // Fill DP table from bottom to top
        for (int i = m - 2; i >= 0; i--) {
            for (int j1 = 0; j1 < n; j1++) {
                for (int j2 = 0; j2 < n; j2++) {
                    int maxi = -1e9;
                    for (int dj1 = -1; dj1 <= 1; dj1++) {
                        for (int dj2 = -1; dj2 <= 1; dj2++) {
                            int value = (j1 == j2 ? grid[i][j1] : grid[i][j1] + grid[i][j2]);
                            int nj1 = j1 + dj1;
                            int nj2 = j2 + dj2;
                            if (nj1 >= 0 && nj1 < n && nj2 >= 0 && nj2 < n)
                                value += next[nj1][nj2];
                            else
                                value += -1e9;
                            maxi = max(maxi, value);
                        }
                    }
                    curr[j1][j2] = maxi;
                }
            }
            next = curr; // move current row up
        }

        return next[0][n - 1];
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int rows, cols;
        cin >> cols >> rows;  // ✅ input is "7 5" (cols rows)
        vector<vector<int>> grid(rows, vector<int>(cols));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int result = obj.cherryPickup(grid);
        cout << result << endl;
    }
    return 0;
}