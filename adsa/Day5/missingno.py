class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        r=0
        for i in range(n+1):
            r ^= i
        for i in range(n):
            r ^= nums[i]
        return r

nums = list(map(int, input().split()))
sol = Solution()
x = sol.missingNumber(nums)
print(x)  # Print the missing number