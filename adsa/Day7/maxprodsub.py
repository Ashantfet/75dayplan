class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        maxprod = nums[0]
        minprod = nums[0]
        result = nums[0]
        
        for i in range(1, n):
            current = nums[i]
            
            if current < 0:
                maxprod, minprod = minprod, maxprod
            
            maxprod = max(current, maxprod * current)
            minprod = min(current, minprod * current)
            
            result = max(result, maxprod)
        
        return result

nums = list(map(int, input().split()))
sol = Solution().maxProduct(nums)
print(sol)