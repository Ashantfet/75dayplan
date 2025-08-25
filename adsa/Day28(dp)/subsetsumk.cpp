#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// int fun(int i,int k,vector<int>& arr,vector<vector<int>>& dp){
// 	if(k==0) return 1;
// 	if(i==0) return (arr[i]==k);
// 	if(dp[i][k]!=-1) return dp[i][k];
// 	int not_pick= fun(i-1,k,arr,dp);
// 	int pick=0;
// 	if(arr[i]<=k) pick=fun(i-1,k-arr[i],arr,dp);
// 	return dp[i][k]=pick+not_pick;
// }
// int findWays(vector<int>& arr, int k)
// {
// 	int n=arr.size();
// 	// vector<vector<int>> dp(n,vector<int>(k+1,-1));
// 	// return fun(n-1,k,arr,dp);
// 	vector<vector<int>> dp(n,vector<int>(k+1,0));
// 	vector<int> prev(k+1,0),curr(k+1,0);
//     if (arr[0] == 0) {
//         dp[0][0] = 2; 
//     } else {
//         dp[0][0] = 1; 
//         if (arr[0] <= k) dp[0][arr[0]] = 1;
//     }
// 	for(int i=1;i<n;i++){
// 		for(int s=0;s<=k;s++){
// 			int not_pick=dp[i-1][s];
// 			int pick=0;
// 			if(arr[i]<=s) pick=dp[i-1][s-arr[i]];
// 			dp[i][s]=pick+not_pick;
// 		}
// 	}
// 	return dp[n-1][k];

// }

const int MOD = 1e9 + 7;
int findWays(vector<int>& arr, int k)
{
    int n = arr.size();
    vector<int> prev(k+1, 0);

    // Base case
    prev[0] = 1;
    if (arr[0] == 0) prev[0] = 2;  // two ways: pick or not pick
    else if (arr[0] <= k) prev[arr[0]] = 1;

    for (int i = 1; i < n; i++) {
        vector<int> curr(k+1, 0);
        for (int s = 0; s <= k; s++) {
            int not_pick = prev[s];
            int pick = 0;
            if (arr[i] <= s) pick = prev[s - arr[i]];
            curr[s] = (pick + not_pick) % MOD;
        }
        prev.swap(curr);
    }

    return prev[k];
}
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << findWays(arr, k) << "\n";
    return 0;
}