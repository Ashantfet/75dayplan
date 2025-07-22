class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        ans =0
        for num in nums:
            ans ^=num
        return ans

nums = list(map(int, input().split()))
sol = Solution()
print(sol.singleNumber(nums))