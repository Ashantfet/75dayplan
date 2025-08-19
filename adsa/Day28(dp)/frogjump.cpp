#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// // int f(int i,vector<int> &heights,vector<int> &dp){
// //     if (i==0) return 0;
// //     if (dp[i]!=-1) return dp[i];
// //     int left= f(i-1,heights,dp) +abs(heights[i]-heights[i-1]);
// //     int right =INT_MAX;
// //     if(i>1) right = f(i-2,heights,dp) +abs(heights[i]-heights[i-2]);
// //     return dp[i]=min(left,right);
// // }
// // int frogJump(int n, vector<int> &heights)
// // {
// //     // Write your code here.
// //     vector<int> dp(n+1,-1);
// //     return f(n-1,heights,dp);
// // }
// int frogJump(int n, vector<int> &heights){
//     vector<int> dp(n,0);
//     dp[0]=0;
//     for(int i=1;i<n;i++){
//         int fs=dp[i-1] +abs(heights[i]-heights[i-1]);
//         int ss=INT_MAX;
//         if (i>1) ss=dp[i-2] + abs(heights[i]-heights[i-2]);
//         dp[i]=min(ss,fs);

//     }
//     return dp[n-1];
// }
int frogJump(int n, vector<int> &heights){
    int prev=0;
    int prev2=0;
    for(int i=1;i<n;i++){
        int fs=prev +abs(heights[i]-heights[i-1]);
        int ss=INT_MAX;
        if (i>1) ss=prev2 + abs(heights[i]-heights[i-2]);
        int curri=min(ss,fs);
        prev2=prev;
        prev=curri;
    }
    return prev;
}


int main() {
    // Example usage
    vector<int> heights = {10, 20, 30, 10};
    int n = heights.size();
    int result = frogJump(n, heights);
    
    // Output the result
    cout << result << endl;
    return 0;
}