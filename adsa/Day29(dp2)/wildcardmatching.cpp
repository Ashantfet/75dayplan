#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// #include <bits/stdc++.h>
// int fun(int i, int j, string &pattern, string &text, vector<vector<int>> &dp) {
//     if (i == 0 && j == 0) return 1;
//     if (i == 0 && j > 0) return 0;
//     if (j == 0 && i > 0) {
//         // pattern must be all '*'
//         for (int k = 0; k < i; k++) {
//             if (pattern[k] != '*') return 0;
//         }
//         return 1;
//     }

//     if (dp[i][j] != -1) return dp[i][j];

//     if (pattern[i-1] == text[j-1] || pattern[i-1] == '?')
//         return dp[i][j] = fun(i-1, j-1, pattern, text, dp);

//     if (pattern[i-1] == '*')
//         return dp[i][j] = (fun(i-1, j, pattern, text, dp) || fun(i, j-1, pattern, text, dp));

//     return dp[i][j] = 0;
// }

// bool wildcardMatching(string pattern, string text) {
//     int m = pattern.size();
//     int n = text.size();
//     vector<vector<int>> dp(m+1, vector<int>(n+1, -1));
//     return fun(m, n, pattern, text, dp);
// }

bool wildcardMatching(string pattern, string text) {
    int m = pattern.size();
    int n = text.size();

    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));

    // base case
    dp[0][0] = true;

    // pattern vs empty text
    for (int i = 1; i <= m; i++) {
        bool allStars = true;
        for (int k = 0; k < i; k++) {
            if (pattern[k] != '*') { allStars = false; break; }
        }
        dp[i][0] = allStars;
    }

    // fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (pattern[i-1] == text[j-1] || pattern[i-1] == '?') {
                dp[i][j] = dp[i-1][j-1];
            }
            else if (pattern[i-1] == '*') {
                dp[i][j] = dp[i-1][j] || dp[i][j-1];
            }
            else {
                dp[i][j] = false;
            }
        }
    }

    return dp[m][n];
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        string pattern, text;
        cin >> pattern >> text;
        cout << (wildcardMatching(pattern, text) ? "true" : "false") << endl;
    }
    return 0;
}