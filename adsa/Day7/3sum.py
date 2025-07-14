# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         n = len(nums)
#         my_set =set()
#         for i in range (n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if(nums[i]+nums[j]+nums[k]==0):
#                         temp = [nums[i],nums[j],nums[k]]
#                         temp.sort()
#                         my_set.add(tuple(temp))
#             return [list(ans) for ans in my_set]

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         n = len(nums)
#         result = set()
#         for i in range(n):
#             myset = set()
#             for j in range(i+1,n):
#                 third = -(nums[i]+nums[j])
#                 if third in myset:
#                     temp = [nums[i],nums[j],third]
#                     temp.sort()
#                     result.add(tuple(temp))
#                 myset.add(nums[j])
#         return [list(ans) for ans in result]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                sum = nums[i] +nums[j] +nums[k]
                if sum <0 :
                    j+=1
                elif sum >0:
                    k-=1
                else:
                    temp =[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and  nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans

nums = list(map(int, input().split()))
sol = Solution().threeSum(nums)
print(sol)