class Solution:
    def isArmstrong(self, n: int) -> bool:

        num = n
        ans = 0
        lod = len(str(num))
        while num >0:
            last = num % 10
            num = num // 10
            ans += last ** lod
        if n == ans:
            return True
        else:
            return False
        
x=int(input())
sol=Solution()
print(sol.isArmstrong(x))