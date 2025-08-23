
// User function Template for C++
#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
//   private:
//     int fun(int i,int j,vector<vector<int>>& mat,vector<vector<int>>& dp){
//         int m=mat.size();
//         int n=mat[0].size();
//         if(j<0 || j>=n) return -1e9;
//         if(i==0) return mat[0][j];
//         if(dp[i][j]!=-1) return dp[i][j];
        
//         int s=mat[i][j]+fun(i-1,j,mat,dp);
//         int ld=mat[i][j]+fun(i-1,j-1,mat,dp);
//         int rd=mat[i][j]+fun(i-1,j+1,mat,dp);
//         return dp[i][j]=max({s,ld,rd});
        
        
//     }
//   public:
//     int maximumPath(vector<vector<int>>& mat) {
//         // code here
//         int m=mat.size();
//         int n=mat[0].size();
//         int maxi=-1e9;
//         vector<vector<int>> dp(m,vector<int>(n,-1));
        
//         for(int j=0;j<m;j++){
//             maxi=max(maxi,fun(n-1,j,mat,dp));
//         }
//         return maxi;
//     }
//   public:
//     int maximumPath(vector<vector<int>>& mat) {
//         // code here
//         int m=mat.size();
//         int n=mat[0].size();
//         int maxi=-1e9;
//         vector<vector<int>> dp(m,vector<int>(n,-1));
        
//         for(int i=0;i<n;i++) dp[0][i]=mat[0][i];
//         for(int i=1;i<m;i++){
//             for(int j=0;j<n;j++){
//                 int u=mat[i][j]+dp[i-1][j];
//                 int ld = (j > 0)     ? mat[i][j] + dp[i-1][j-1] : -1e9;
//                 int rd = (j < n-1)   ? mat[i][j] + dp[i-1][j+1] : -1e9;
//                 dp[i][j]=max({u,ld,rd});
//             }
//         }
//         for (int j = 0; j < n; j++) {
//             maxi = max(maxi, dp[m-1][j]);
//         }
//         return maxi;
//     }
  public:
    int maximumPath(vector<vector<int>>& mat) {
        // code here
        int m=mat.size();
        int n=mat[0].size();
        int maxi=-1e9;
        vector<int> prev(n,0);
        
        for(int i=0;i<n;i++) prev[i]=mat[0][i];
        for(int i=1;i<m;i++){
            vector<int> curr(n,0);
            for(int j=0;j<n;j++){
                int u=mat[i][j]+prev[j];
                int ld = (j > 0)     ? mat[i][j] + prev[j-1] : -1e9;
                int rd = (j < n-1)   ? mat[i][j] + prev[j+1] : -1e9;
                curr[j]=max({u,ld,rd});
            }
            prev.swap(curr);
        }
        for (int j = 0; j < n; j++) {
            maxi = max(maxi, prev[j]);
        }
        return maxi;
    }
};
int main(){
    Solution obj;
    vector<vector<int>> mat={{1,2,3},{4,5,6},{7,8,9}};
    cout<<obj.maximumPath(mat);
}