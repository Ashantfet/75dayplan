// User function Template for C++
#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
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
    bool canPartition(vector<int>& nums) {
        int n=nums.size();
        int totsum=0;
        for(int i=0;i<n;i++) totsum+=nums[i];
        if(totsum%2!=0) return false;
        int target=totsum/2;
        return subsetSumToK(n,target,nums);
    }
};
int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution obj;
        bool ans = obj.canPartition(arr);
        if(ans) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}