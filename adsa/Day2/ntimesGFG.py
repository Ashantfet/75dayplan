#print GFG n times
class Solution:
    def printGfg(self, n):
        # Code here
        if n==1:
            print("GFG",end=" ")
            return
        self.printGfg(n-1)
        print("GFG",end=" ")

x=int(input())
ob = Solution()
ob.printGfg(x)