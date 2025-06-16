class Solution:
    # def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     startpoint = 0
    #     ans = []
    #     for i in range(n):
    #         if nums[i] == 0:
    #             ans.append(i - startpoint)
    #             startpoint = i + 1
    #     ans.append(n - startpoint)
    #     return max(ans)
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        max_count =0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                max_count =max(max_count,count)
                count = 0
        return max(max_count,count)

a = list(map(int, input().split()))
sol = Solution()
x = sol.findMaxConsecutiveOnes(a)
print(x)  # Print the maximum count of consecutive 1's