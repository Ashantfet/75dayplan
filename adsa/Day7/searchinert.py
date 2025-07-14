class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        ans=0
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                l=mid+1
            elif nums[mid] < target:
                ans =mid+1
                l= mid+1
            else:
                r=mid-1
        return ans

nums = list(map(int, input().split()))
target = int(input())
sol = Solution().searchInsert(nums, target)
print(sol)