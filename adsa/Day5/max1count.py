class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        startpoint = 0
        ans = []
        for i in range(n):
            if nums[i] == 0:
                ans.append(i - startpoint)
                startpoint = i + 1
        ans.append(n - startpoint)
        return max(ans)

a = list(map(int, input().split()))
sol = Solution()
x = sol.findMaxConsecutiveOnes(a)
print(x)  # Print the maximum count of consecutive 1's