#include <bits/stdc++.h> 
#include <iostream>
#include <vector>
using namespace std;

int minimumCoins(int P) {
    vector<int> coins = {1000, 500, 100, 50, 20, 10, 5, 2, 1};
    int count = 0;

    for (int coin : coins) {
        if (P >= coin) {
            count += P / coin;   
            P %= coin;           
        }
    }
    return count;
}
int main() {
    int P;
    std::cin >> P;
    std::cout << minimumCoins(P) << std::endl;
    return 0;
}