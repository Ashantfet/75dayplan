#User function Template for python3
class Solution:
    def countFactors (self, N):
        # code here
        result=0
        for i in range(1,int(N**0.5)+1):
            if N%i==0:
                result+=1
                if N//i!=i:
                    result+=1
        return result
x=int(input())
sol=Solution()
print(sol.countFactors(x))