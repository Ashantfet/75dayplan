class Solution:
    def countFreq(self, arr, target):
        #code here
        n= len(arr)
        l=0
        r=n-1
        while(l<=r):
            mid =(l+r)//2
            if arr[mid] <target:
                l=mid+1
            elif arr[mid] > target:
                r= mid-1
            else:
                start = mid
                end = mid
                while start > 0 and arr[start - 1] == target:
                    start -= 1
                while end < n - 1 and arr[end + 1] == target:
                    end += 1
                return end-start+1
        return 0
arr = list(map(int, input().split()))
x = int(input())
sol = Solution()
result = sol.countFreq(arr, x)
print(result)