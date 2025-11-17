#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// int fun(int i, int j, string &str1, string &str2, vector<vector<int>> &dp) {
//     if (i == 0) return j;  // need j insertions
//     if (j == 0) return i;  // need i deletions

//     if (dp[i][j] != -1) return dp[i][j];

//     if (str1[i-1] == str2[j-1]) 
//         return dp[i][j] = fun(i-1, j-1, str1, str2, dp);

//     return dp[i][j] = 1 + min({
//         fun(i, j-1, str1, str2, dp),   // insertion
//         fun(i-1, j-1, str1, str2, dp), // replacement
//         fun(i-1, j, str1, str2, dp)    // deletion
//     });
// }

int editDistance(string str1, string str2) {
    int m = str1.size();
    int n = str2.size();
    // vector<vector<int>> dp(m+1, vector<int>(n+1, -1));
    // return fun(m, n, str1, str2, dp);
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({
                    dp[i][j-1],   // insertion
                    dp[i-1][j-1], // replacement
                    dp[i-1][j]    // deletion
                });
            }
        }
    }

    return dp[m][n];
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s1, s2;
        cin >> s1 >> s2;
        cout << editDistance(s1, s2) << endl;
    }
    return 0;
}