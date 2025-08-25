#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
int minSubsetSumDifference(vector<int>& arr, int n)
{
	// Write your code here.

	long long totsum = 0;
	for (int x : arr) totsum += x;

	vector<bool> dp(totsum + 1, false);
	dp[0] = true;

	for (int num : arr) {
		for (int target = totsum; target >= num; target--) {
			dp[target] = dp[target] || dp[target - num];
		}
	}

	int mini = totsum;
	for (int s1 = 0; s1 <= totsum / 2; s1++) {
		if (dp[s1]) {
			int s2 = totsum - s1;
			mini = min(mini, abs(s2 - s1));
		}
	}
	return mini;
}
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << minSubsetSumDifference(arr, n) << "\n";
    return 0;
}