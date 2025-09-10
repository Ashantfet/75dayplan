#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
// private:
//     int fun(int ind,int amount,vector<int>& coins,vector<vector<int>> &dp){
//         if(ind==0) return ((amount%coins[0])==0);//base case
//         if(dp[ind][amount]!=-1) return dp[ind][amount];
//         int nottake= fun(ind-1,amount,coins,dp);
//         int take =0;
//         if(coins[ind]<=amount) take =fun(ind,amount-coins[ind],coins,dp);
//         return dp[ind][amount]=(take+nottake);
//     }
public:
    // int change(int amount, vector<int>& coins) {
    //     int n=coins.size();
    //     vector<vector<int>> dp(n,vector<int>(amount+1,-1));
    //     return fun(n-1,amount,coins,dp);
    // }
    int change(int amount, vector<int>& coins) {
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int>(amount+1, 0));

        // base case: using only coin[0]
        for (int amt = 0; amt <= amount; amt++) {
            dp[0][amt] = (amt % coins[0] == 0);
        }

        for (int i = 1; i < n; i++) {
            for (int amt = 0; amt <= amount; amt++) {
                long long notTake = dp[i-1][amt];
                long long take = 0;
                if (coins[i] <= amt) take = dp[i][amt - coins[i]];
                dp[i][amt] = (int)(take + notTake);  // safe, guaranteed ≤ 2e9
            }
        }
        return dp[n-1][amount];
    }

};
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, amount;
        cin >> n >> amount;
        vector<int> coins(n);
        for (int i = 0; i < n; i++) {
            cin >> coins[i];
        }
        Solution obj;
        cout << obj.change(amount, coins) << endl;
    }
    return 0;
}

