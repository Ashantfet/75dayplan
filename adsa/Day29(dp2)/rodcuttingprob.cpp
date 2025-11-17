#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// int fun(int ind,int n,vector<int> &price,vector<vector<int>> &dp){
// 	if(ind==0) return n*price[0];
// 	if(dp[ind][n]!=-1) return dp[ind][n];
// 	int nottake=fun(ind-1,n,price,dp);
// 	int take=INT_MIN;
// 	int rod=ind+1;
// 	if(rod<=n)
// 	take=price[ind]+fun(ind,n-rod,price,dp);
// 	return dp[ind][n]=max(take,nottake);
// }
int cutRod(vector<int> &price, int n)
{
	// Write your code here.
	// vector<vector<int>> dp(n,vector<int>(n+1,-1));
	// return fun(n-1,n,price,dp);
	vector<vector<int>> dp(n,vector<int>(n+1,0));
	for(int i=0;i<=n;i++){
		dp[0][i]=i*price[0];
	}
	for(int ind=1;ind<n;ind++){
			int rod=ind+1;
		for(int N=0;N<=n;N++){
			int nottake=dp[ind-1][N];
			int take=INT_MIN;

			if(rod<=N)
			take=price[ind]+dp[ind][N-rod];
			dp[ind][N]=max(take,nottake);
		}
	}
	return dp[n-1][n];
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> price(n);
        for (int i = 0; i < n; i++) {
            cin >> price[i];
        }
        cout << cutRod(price, n) << endl;
    }
    return 0;
}