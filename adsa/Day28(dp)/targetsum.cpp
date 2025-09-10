#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
private:
    int findWays(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> prev(k+1, 0);

        // Base case
        prev[0] = 1;
        if (arr[0] == 0) prev[0] = 2;  
        else if (arr[0] <= k) prev[arr[0]] = 1;

        for (int i = 1; i < n; i++) {
            vector<int> curr(k+1, 0);
            for (int s = 0; s <= k; s++) {
                int not_pick = prev[s];
                int pick = 0;
                if (arr[i] <= s) pick = prev[s - arr[i]];
                curr[s] = (pick + not_pick); 
            }
            prev.swap(curr);
        }

        return prev[k];
    }

    int countPartitions(int n, int d, vector<int> &arr) {
        long long totsum = 0;
        for (int x : arr) totsum += x;

        if (totsum < d || (totsum - d) % 2 != 0) return 0;

        int s2 = (totsum - d) / 2;
        return findWays(arr, s2);
    }

public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return countPartitions(nums.size(),target,nums);
    }
};
int main() {
    int n, target;
    cin >> n >> target;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    Solution obj;
    cout << obj.findTargetSumWays(nums, target) << endl;
    return 0;
}