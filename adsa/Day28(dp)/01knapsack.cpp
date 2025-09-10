#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;

// int fun(int ind, int W, const vector<int>& weight, const vector<int>& value, int n, vector<vector<int>>& dp) {
//     if (ind == 0) {
//         if (weight[0] <= W) return value[0];
//         return 0;
//     }
//     if (dp[ind][W] != -1) return dp[ind][W];

//     int nottake = fun(ind - 1, W, weight, value, n, dp);
//     int take = INT_MIN;
//     if (weight[ind] <= W) {
//         take = value[ind] + fun(ind - 1, W - weight[ind], weight, value, n, dp);
//     }
//     return dp[ind][W] = max(take, nottake);
// }

// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) {
//     vector<vector<int>> dp(n, vector<int>(maxWeight + 1, -1));
//     return fun(n - 1, maxWeight, weight, value, n, dp);
// }


// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) {
//     vector<vector<int>> dp(n, vector<int>(maxWeight + 1, 0));

//     for (int w = weight[0]; w <= maxWeight; w++) {
//         dp[0][w] = value[0]; 
//     }


//     for (int i = 1; i < n; i++) {
//         for (int w = 0; w <= maxWeight; w++) {
//             int notTake = dp[i-1][w];
//             int take = INT_MIN;
//             if (weight[i] <= w) {
//                 take = value[i] + dp[i-1][w - weight[i]];
//             }
//             dp[i][w] = max(take, notTake);
//         }
//     }

//     return dp[n-1][maxWeight];
// }

// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) {
//     vector<int> prev(maxWeight+1,0),curr(maxWeight+1,0);
//     for (int w = weight[0]; w <= maxWeight; w++) {
//         prev[w] = value[0]; 
//     }


//     for (int i = 1; i < n; i++) {
//         for (int w = 0; w <= maxWeight; w++) {
//             int notTake = prev[w];
//             int take = INT_MIN;
//             if (weight[i] <= w) {
//                 take = value[i] + prev[w - weight[i]];
//             }
//             curr[w] = max(take, notTake);
//         }
//         prev.swap(curr);
//     }

//     return prev[maxWeight];
// }
int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) {
    vector<int> dp(maxWeight+1, 0);

    // Base case
    for (int w = weight[0]; w <= maxWeight; w++) {
        dp[w] = value[0];
    }

    for (int i = 1; i < n; i++) {
        for (int w = maxWeight; w >= weight[i]; w--) {
            dp[w] = max(dp[w], value[i] + dp[w - weight[i]]);
        }
    }

    return dp[maxWeight];
}
int main() {
    int n, maxWeight;
    cin >> n >> maxWeight;
    vector<int> weight(n), value(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> value[i];
    }
    cout << knapsack(weight, value, n, maxWeight) << endl;
    return 0;
}