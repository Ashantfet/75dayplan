class Solution:
    def twoOddNum(self, arr):
        #code here 
        ans = 0
        for num in arr:
            ans ^=num
        setbit = ans &(-ans)
        x=0
        y=0
        for num in arr:
            if num & setbit:
                x^=num
            else:
                y^=num
        return [x,y] if x>y else [y,x]  
arr = list(map(int, input().split()))
sol = Solution()
print(*sol.twoOddNum(arr))