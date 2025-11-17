#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
int longestCommonSubsequence(string text1, string text2) {
    int n = text1.size();
    int m = text2.size();

    vector<int> prev(m+1, 0), curr(m+1, 0);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (text1[i-1] == text2[j-1]) 
                curr[j] = 1 + prev[j-1];
            else 
                curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;  // move to next row
    }
    return prev[m];
}
int canYouMake(string &s1, string &s2){
    // Write your code here.
    int n=s1.size();
    int m=s2.size();
    return n+m-2*longestCommonSubsequence(s1,s2);
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;

        string s1, s2;
        cin >> s1 >> s2;
        cout << canYouMake( s1, s2) << endl;
    }
    return 0;
}