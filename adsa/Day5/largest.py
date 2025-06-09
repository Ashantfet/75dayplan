class Solution:
    def largest(self, arr):
        # code here
        n=len(arr)
        max=arr[0]
        for i in range(1,n):
            if(arr[i]>=max):
                max=arr[i]
        return max

# Driver Code
arr = list(map(int, input().split()))
sol = Solution()
x=sol.largest(arr)
print(x)