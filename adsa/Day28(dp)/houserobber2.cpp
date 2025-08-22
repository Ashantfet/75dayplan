#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
class Solution {
private:
    
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
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int> temp1,temp2;
        if (n==1) return nums[0];
        for(int i=0;i<n;i++){
            if(i!=0)temp1.push_back(nums[i]);
            if(i!=n-1)temp2.push_back(nums[i]); 
        }
        return max(maximumNonAdjacentSum(temp1),maximumNonAdjacentSum(temp2));
    }
    
};
int main() {
    // Example usage
    vector<int> nums = {2, 3, 2, 1, 3, 1};
    Solution sol;
    int result = sol.rob(nums);
    
    // Output the result
    cout << result << endl; // Output: 7
    return 0;
}