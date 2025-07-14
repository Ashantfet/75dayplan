# class Solution:
#     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
#         n = len(nums)
#         my_set =set()
#         for i in range (n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     for l in range(k+1,n):
#                         if(nums[i]+nums[j]+nums[k] +nums[l]==target):
#                             temp = [nums[i],nums[j],nums[k],nums[l]]
#                             temp.sort()
#                             my_set.add(tuple(temp))
#         return [list(ans) for ans in my_set]

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n= len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    total =nums[i] +nums[j] + nums[k] + nums[l]
                    if total ==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and  nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                    elif total < target :
                        k+=1
                    else:
                        l-=1
        return ans
    
nums = list(map(int, input().split()))
target = int(input())
sol = Solution().fourSum(nums, target)
print(sol)