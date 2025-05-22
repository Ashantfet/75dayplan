#prints reverse number without using loops
class Solution:
    def printNos(self, n):
        # Code here
        if n==1:
            print(1,end =" ")
            return
        print(n,end=" ")
        self.printNos(n-1)
        
x=int(input())
ob = Solution()
ob.printNos(x)