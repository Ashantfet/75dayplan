class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        mini = float('inf') 

        while l <= r:
            mid = (l + r) // 2
            mini = min(mini, nums[mid])  

            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] <= nums[r]:
                
                mini = min(mini, nums[mid])
                r = mid - 1
            else:
                
                mini = min(mini, nums[l])
                l = mid + 1

        return mini
arr = list(map(int, input().split()))
sol = Solution()
result = sol.findMin(arr)
print(result)   