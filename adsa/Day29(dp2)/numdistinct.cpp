#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int i,int j,string s, string t,vector<vector<int>> &dp){
//         if(j==0) return 1;
//         if(i==0) return 0;
//         if(dp[i][j]!= -1) return dp[i][j];
//         if(s[i-1]==t[j-1]) return dp[i][j]=(fun(i-1,j-1,s,t,dp)+fun(i-1,j,s,t,dp));
//         return dp[i][j]=fun(i-1,j,s,t,dp);
//     }
public:
    int numDistinct(string s, string t) {
        int m=s.size();
        int n=t.size();
        // vector<vector<int>> dp(m+1,vector<int>(n+1,-1));
        // return fun(m,n,s,t,dp);
        vector<vector<double>> dp(m+1,vector<double>(n+1,0));
        for (int i = 0; i <= m; i++) dp[i][0] = 1;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(s[i-1]==t[j-1]){
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j];
                }
                else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return (int)dp[m][n];
    }
};
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s1, s2;
        cin >> s1 >> s2;
        Solution obj;
        cout << obj.numDistinct(s1, s2) << endl;
    }
    return 0;
}