// User function Template for C++
#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// bool fun(int n,int k,vector<int> &arr,vector<vector<int>> &dp){

//     if (k==0) return true;
//     if(n==0) return arr[0]==k;
//     if(dp[n][k]!=-1) return dp[n][k];
//     bool not_take=fun(n-1,k,arr,dp);
//     bool take=false;
//     if (arr[n] <= k)
//     take=fun(n-1,k-arr[n],arr,dp);
//     return dp[n][k]=take |not_take;
// } 
// bool subsetSumToK(int n, int k, vector<int> &arr) {
//     // Write your code here.
//     vector<vector<int>> dp(n,vector<int>(k+1,-1));
//     return fun(n-1,k,arr,dp);
// }
// bool subsetSumToK(int n, int k, vector<int> &arr) {
//     // Write your code here.
//     vector<bool> prev(k+1,0),cur(k+1,0);
//     prev[0]=true;
//      if (arr[0] <= k) prev[arr[0]] = true;
//     for(int ind=1;ind<n;ind++){
//         cur[0] = true;
//         for(int target=0;target<=k;target++){
//             bool not_take=prev[target];
//             bool take=false;
//             if (arr[ind] <= target)
//             take=prev[target-arr[ind]];
//             cur[target]=take |not_take;
//         }
//         prev.swap(cur);
//     }
//     return prev[k];
// }
bool subsetSumToK(int n, int k, vector<int> &arr) {
    vector<bool> dp(k+1, false);

    dp[0] = true;  // sum 0 is always possible
    if (arr[0] <= k) dp[arr[0]] = true;

    for (int ind = 1; ind < n; ind++) {
        for (int target = k; target >= arr[ind]; target--) {
            dp[target] = dp[target] || dp[target - arr[ind]];
        }
    }
    return dp[k];
}
int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        if (subsetSumToK(n, k, arr)) cout << "true" << endl;
        else cout << "false" << endl;
    }

    return 0;
}

