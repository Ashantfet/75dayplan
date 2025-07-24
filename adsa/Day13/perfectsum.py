class Solution:
    def perfectSum(self, arr, target):
        mod = 10**9 + 7
        n = len(arr)
        memo = {}

        def backtrack(index, total):
            if index == n:
                return 1 if total == target else 0

            if (index, total) in memo:
                return memo[(index, total)]

            # Include current element
            pick = backtrack(index + 1, total + arr[index])
            # Exclude current element
            not_pick = backtrack(index + 1, total)

            memo[(index, total)] = (pick + not_pick) % mod
            return memo[(index, total)]

        return backtrack(0, 0)

# #User function Template for python3
# class Solution:
#     def perfectSum(self, arr, target):
#         # code here
#         return self.backtrack(0,0,target,arr)

#     def backtrack(self,index,total,target,nums):
#         if index == len(nums):
#             return 1 if total == target else 0
#         elif total >target:
#             return 0
#         if index >=len(nums):
#             return 0
#         sum = total + nums[index]
#         pick=self.backtrack(index+1,sum,target,nums)
#         sum = total
#         not_pick = self.backtrack(index+1,sum,target,nums)
#         return pick+not_pick

arr = list(map(int, input().split()))
target = int(input())
sol = Solution()
print(sol.perfectSum(arr, target))