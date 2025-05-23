class Solution:
    def factorialNumbers(self, n):
    	#code here 
        fact=1
        i = 1
        result = []
        
        while fact <= n:
            result.append(fact)
            i += 1
            fact *= i
        
        return result
x = int(input())
ob = Solution()
print(ob.factorialNumbers(x)) 