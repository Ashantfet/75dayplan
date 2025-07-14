# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:

#         n= len(prices)
#         profit = 0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if prices[j]- prices[i] > profit:
#                     profit = max(profit,prices[j]-prices[i])
        
#         return profit
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
                min_price = min(min_price, price)
                max_profit = max(max_profit, price - min_price)

        return max_profit
prices = list(map(int, input().split()))
sol = Solution().maxProfit(prices)
print(sol)