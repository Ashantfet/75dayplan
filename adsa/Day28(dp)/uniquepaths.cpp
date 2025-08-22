#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;
int uniquePaths(int m, int n) {
	// Write your code here.
	vector<int> prev(n,0);
	for(int i=0;i<m;i++){
		vector<int> temp(n,0);
		for(int j=0;j<n;j++){
			if(i==0 and j==0) temp[j] = 1; 
			else{
				int up=0;
				int left=0;
				if(i>0) up=prev[j];
				if(j>0) left=temp[j-1];
				temp[j]=up+left;
			}
		}
		prev.swap(temp);
	}
	return prev[n-1];

}
int main() {
    // Example usage
    int m = 3, n = 7;
    int result = uniquePaths(m, n);
    
    // Output the result
    cout << result << endl; // Output: 28
    return 0;
}