class Solution:
    def isPrime(self, n):
        # code here
        if(n==1):
            return False
        if(n==2):
            return True
        result=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                result+=1
                if n//i!=i:
                    result+=1
        if(result==2):
            return True
        else:
            return False
x=int(input())
sol=Solution()
print(sol.isPrime(x))