class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n= len(nums)
        if n==0:
            return [-1 ,-1]
        l=0
        r=n-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] <target:
                l=mid+1
            elif nums[mid] > target:
                r= mid-1
            else:
                start = mid
                end = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < n - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
        return [-1,-1]

arr = list(map(int, input().split()))
x = int(input())
sol = Solution()
result = sol.searchRange(arr, x)
print(result)