class Solution:
    def jump(self, nums: list[int]) -> int:
        n= len(nums)
        jump =0
        right , left =0,0

        farthest =0
        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            if i == right:
                jump+=1
                right = farthest
        return jump
nums = list(map(int, input().split()))
solution = Solution()
print(solution.jump(nums))