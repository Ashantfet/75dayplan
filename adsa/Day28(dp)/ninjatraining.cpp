#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
// int f(int day,int last,vector<vector<int>> &points,vector<vector<int>> &dp){
//     if(day==0){
//         int maxi =0;
//         for(int task=0;task<3;task++){
//             if(task!=last){
//                 maxi= max(maxi,points[0][task]);
//             }
//         }
//         return maxi;
//     }
//     if(dp[day][last]!=-1) return dp[day][last];
//     int maxi=0;
//     for(int task=0;task<3;task++){
//         if(task!=last){
//             int point= points[day][task] + f(day-1,task,points,dp);
//             maxi=max(maxi,point);
//         }
//     }
//     return dp[day][last]=maxi;
// }
#include <algorithm>  // gives std::max overloads
// int ninjaTraining(int n, vector<vector<int>> &points)
// {
//     // Write your code here.
//     vector<vector<int>> dp(n,vector<int> (4,0));//intialize with -1 for memoziation
//     //return f(n-1,3,points,dp);
//     dp[0][0] =max(points[0][1],points[0][2]);
//     dp[0][1] =max(points[0][0],points[0][2]);
//     dp[0][2] =max(points[0][0],points[0][1]);
//     dp[0][3] =max({points[0][0],points[0][1],points[0][2]});
//     for(int day=1;day<n;day++){
//         for(int last=0;last<4;last++){
//             dp[day][last]=0;
//             for(int task=0;task<3;task++){
//                 if (task!=last){
//                     int point = points[day][task]+ dp[day-1][task];
//                     dp[day][last]=max(dp[day][last],point);
//                 }
//             }
//         }
//     }
//     return dp[n-1][3];

// }

int ninjaTraining(int n, vector<vector<int>> &points)
{
    // Write your code here.
    vector<int> prev(4,0);//intialize with -1 for memoziation
    //return f(n-1,3,points,dp);
    prev[0] =max(points[0][1],points[0][2]);
    prev[1] =max(points[0][0],points[0][2]);
    prev[2] =max(points[0][0],points[0][1]);
    prev[3] =max({points[0][0],points[0][1],points[0][2]});
    for(int day=1;day<n;day++){
        vector<int> temp(4,0);
        for(int last=0;last<4;last++){
            temp[last]=0;
            for(int task=0;task<3;task++){
                if (task!=last){
                    int point = points[day][task]+ prev[task];
                    temp[last]=max(temp[last],point);
                }
            }
        }
        prev.swap(temp);
    }
    return prev[3];

}
int main() {
    // Example usage
    int n = 4;
    vector<vector<int>> points = {{2,1,3},{3,4,6},{10,1,6},{8,3,7}};
    int result = ninjaTraining(n, points);
    
    // Output the result
    cout << result << endl; // Output: 11
    return 0;
}