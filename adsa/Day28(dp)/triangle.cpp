#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int i,int j,vector<vector<int>>& triangle,vector<vector<int>>& dp){
//         int n=triangle.size();
//         if(i==n-1) return triangle[n-1][j];
//         if (dp[i][j]!=-1) return dp[i][j];
//         int d=triangle[i][j]+fun(i+1,j,triangle,dp);
//         int dia=triangle[i][j]+fun(i+1,j+1,triangle,dp);
//         return dp[i][j]=min(d,dia);
//     }
public:
    // int minimumTotal(vector<vector<int>>& triangle) {
    //     int n=triangle.size();
    //     vector<vector<int>> dp(n,vector<int>(n,-1));
    //     for(int j=0;j<n;j++){
    //         dp[n-1][j]=triangle[n-1][j];
    //     }
    //     for(int i=n-2;i>=0;i--){
    //         for(int j=i;j>=0;j--){
    //             int d=triangle[i][j]+dp[i+1][j];
    //             int dia=triangle[i][j]+dp[i+1][j+1];
    //             dp[i][j]=min(d,dia);
    //         }
    //     }
    //     return dp[0][0];
    //     //return fun(0,0,triangle,dp);
    // }
    int minimumTotal(vector<vector<int>>& triangle) {
        int n=triangle.size();
        vector<int> front(n,0);
        for(int j=0;j<n;j++){
            front[j]=triangle[n-1][j];
        }
        for(int i=n-2;i>=0;i--){
            vector<int> curr(n,0);
            for(int j=i;j>=0;j--){
                int d=triangle[i][j]+front[j];
                int dia=triangle[i][j]+front[j+1];
                curr[j]=min(d,dia);
            }
            front.swap(curr);
        }
        return front[0];
        //return fun(0,0,triangle,dp);
    }
};
int main(){
    Solution obj;
    vector<vector<int>> triangle={{2},{3,4},{6,5,7},{4,1,8,3}};
    cout<<obj.minimumTotal(triangle);
}