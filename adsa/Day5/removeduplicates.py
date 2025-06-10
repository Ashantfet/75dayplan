class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
    
nums = list(map(int, input().split()))
sol = Solution()
x = sol.removeDuplicates(nums)
print(nums[:x])  # Print the modified array up to the new length