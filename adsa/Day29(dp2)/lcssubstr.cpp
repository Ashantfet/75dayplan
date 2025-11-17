#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
int LCSubStr(string &text1, string &text2)
{
        int n=text1.size();
        int m=text2.size();
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        //return fun(n,m,text1,text2,dp);
        int ans=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(text1[i-1]==text2[j-1]) {
                    dp[i][j]=1+dp[i-1][j-1];
                    ans=max(ans,dp[i][j]);
                }

                else 
                    dp[i][j]=0;
                    
            }
        }
        return ans;
    // Write your code here

}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;

        string s1, s2;
        cin >> s1 >> s2;
        cout << LCSubStr( s1, s2) << endl;
    }
    return 0;
}