#print sum of cubes of first n natural numbers
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n==1:
            return 1
        return (n**3) + self.sumOfSeries(n-1)
x=int(input())
ob = Solution()
print(ob.sumOfSeries(x))