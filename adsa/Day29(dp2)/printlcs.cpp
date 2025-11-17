#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
string longestCommonSubsequence(string s1, string s2) {
	int n=s1.size();
	int m=s2.size();
	vector<vector<int>> dp(n+1,vector<int>(m+1,0));
	//return fun(n,m,text1,text2,dp);
	for(int j=0;j<=m;j++) dp[0][j]=0;
	for(int i=0;i<=n;i++) dp[i][0]=0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			if(s1[i-1]==s2[j-1]) 
				dp[i][j]=1+dp[i-1][j-1];
			else 
				dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
		}
	}
	int len= dp[n][m];
	string ans="";
	for(int i=0;i<len;i++)ans+='$';
	int index=len-1;
	int i=n;
	int j=m;
	while(i>0 && j>0){
		if(s1[i-1]==s2[j-1]){
			ans[index]=s1[i-1];
			index--;
			i--;
			j--;
		}
		else if(dp[i-1][j]>dp[i][j-1]){
			i=i-1;
		}
		else{
			j=j-1;
		}
	}	
	return ans;
}
string findLCS(string &s1, string &s2){
	// Write your code here.
	return longestCommonSubsequence(s1,s2);
	
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;

        string s1, s2;
        cin >> s1 >> s2;
        cout << findLCS( s1, s2) << endl;
    }
    return 0;
}