#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// int maximumNonAdjacentSum(vector<int> &nums){
//     // Write your code here.
//     int n= nums.size();
//     vector<int> dp(n,0);
//     dp[0]=nums[0];
//     int neg =0;
//     for(int i=1;i<n;i++){
//         int take = nums[i];
//         if (i>1) take+=dp[i-2];
//         int nontake=dp[i-1];
//         dp[i]=max(take,nontake);
//     }
//     return dp[n-1];

// }

int maximumNonAdjacentSum(vector<int> &nums){
    int n=nums.size();
    int prev=nums[0];
    int prev2=0;
    for(int i=1;i<n;i++){
        int take=nums[i];
        if (i>1) take+=prev2;
        int nontake=prev;
        int curr=max(take,nontake);
        prev2=prev;
        prev=curr;

    }
    return prev;
}
int main() {
    // Example usage
    vector<int> nums = {2, 4, 6, 2, 5};
    int result = maximumNonAdjacentSum(nums);
    
    // Output the result
    cout << result << endl; // Output: 13
    return 0;
}