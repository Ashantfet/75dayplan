#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int n,int m,string text1, string text2,vector<vector<int>> &dp){
//         if(n==0 || m==0) return 0;
//         if(dp[n][m]!=-1) return dp[n][m];
//         if(text1[n-1]==text2[m-1]) return dp[n][m]=1+fun(n-1,m-1,text1,text2,dp);
//         return dp[n][m]=max(fun(n-1,m,text1,text2,dp),fun(n,m-1,text1,text2,dp));
//     }
public:
    // int longestCommonSubsequence(string text1, string text2) {
    //     int n=text1.size();
    //     int m=text2.size();
    //     vector<vector<int>> dp(n+1,vector<int>(m+1,0));
    //     //return fun(n,m,text1,text2,dp);
    //     for(int j=0;j<=m;j++) dp[0][j]=0;
    //     for(int i=0;i<=n;i++) dp[i][0]=0;
    //     for(int i=1;i<=n;i++){
    //         for(int j=1;j<=m;j++){
    //             if(text1[i-1]==text2[j-1]) 
    //                 dp[i][j]=1+dp[i-1][j-1];
    //             else 
    //                 dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
    //         }
    //     }
    //     return dp[n][m];
    // }

    // int longestCommonSubsequence(string text1, string text2) {
    //     int n = text1.size();
    //     int m = text2.size();

    //     vector<int> prev(m+1, 0), curr(m+1, 0);

    //     for (int i = 1; i <= n; i++) {
    //         for (int j = 1; j <= m; j++) {
    //             if (text1[i-1] == text2[j-1]) 
    //                 curr[j] = 1 + prev[j-1];
    //             else 
    //                 curr[j] = max(prev[j], curr[j-1]);
    //         }
    //         prev = curr;  // move to next row
    //     }
    //     return prev[m];
    // }

    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();

        vector<int> dp(m+1, 0);

        for (int i = 1; i <= n; i++) {
            int prevDiag = 0;  
            for (int j = 1; j <= m; j++) {
                int temp = dp[j];  
                if (text1[i-1] == text2[j-1]) {
                    dp[j] = 1 + prevDiag;
                } else {
                    dp[j] = max(dp[j], dp[j-1]);
                }
                prevDiag = temp;  
            }
        }
        return dp[m];
    }

};
int main() {
    int t;
    cin >> t;
    while (t--) {
        string text1, text2;
        cin >> text1 >> text2;
        Solution obj;
        cout << obj.longestCommonSubsequence(text1, text2) << endl;
    }
    return 0;
}