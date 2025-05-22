#prints numvbers without using loop
class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n==1:
            print(1, end=" ")
            return 
        self.printNos(n-1)
        print(n,end=" ")

x=int(input())
ob = Solution()
ob.printNos(x)