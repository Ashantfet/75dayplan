class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        num =x
        ans =0
        while num>0:
            last=num%10
            num=num//10
            ans=ans*10+last
        if x==ans:
            return True
        else:
            return False

x=int(input())
sol=Solution()
print(sol.isPalindrome(x))