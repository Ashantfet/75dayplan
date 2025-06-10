class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        n=len(arr)
        for i in range (1,n):
            if(arr[i-1]<=arr[i]):
                continue
            else:
                return False
        return True

arr = list(map(int, input().split()))
sol = Solution()
x=sol.arraySortedOrNot(arr)
print(x)