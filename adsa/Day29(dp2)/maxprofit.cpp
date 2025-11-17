#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        int mini=prices[0];
        int maxprofit=0;
        for(int i=1;i<n;i++){
            int cost = prices[i]-mini;
            maxprofit=max(maxprofit,cost);
            mini = min(mini,prices[i]);
        }
        return maxprofit;
        
    }
};
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> prices(n);
        for (int i = 0; i < n; i++) {
            cin >> prices[i];
        }
        Solution obj;
        cout << obj.maxProfit(prices) << endl;
    }
    return 0;
}