class Solution:
    def lcmAndGcd(self, a : int, b : int) -> list[int]:
        # code here
        x,y=abs(a),abs(b)
        while(y!=0):
            x,y=y,x%y
        gcd=x
        lcm =abs(a*b)//gcd if a and b else 0
        return [lcm,gcd]
x,y=map(int,input().split())
sol=Solution()
print(sol.lcmAndGcd(x,y))