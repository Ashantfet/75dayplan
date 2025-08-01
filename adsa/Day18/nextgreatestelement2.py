class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1]*n
        stack =[]
        for i in range(2*n-1,-1,-1):
            curr = nums[i%n]
            while len(stack)!=0 and nums[stack[-1]] <= curr:
                stack.pop()
            if i<n:
                if len(stack)!= 0:
                    ans[i] =nums[stack[-1]]
            stack.append(i%n)
        return ans
nums = list(map(int, input().split()))
solution = Solution()
print(*solution.nextGreaterElements(nums))  