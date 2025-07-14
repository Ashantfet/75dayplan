class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l =0
        n= len(nums)
        r = n-1
        
        while r>=l:
            mid =(l+r)//2
            if(nums[mid]== target):
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1

nums = list(map(int, input().split()))
target = int(input())
sol = Solution().search(nums, target)
print(sol)