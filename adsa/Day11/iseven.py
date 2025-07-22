class Solution:
    def isEven (self, n):
        # code here 
        if n%2==0:
            return True
        return False
n = int(input())
sol = Solution()
print(sol.isEven(n))