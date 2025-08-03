class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxindex =0
        for i in range(0,len(nums)):
            if i>maxindex:
                return False
            maxindex = max(maxindex, i+nums[i])
        return True


nums = list(map(int, input().split()))
solution = Solution()
print(solution.canJump(nums))