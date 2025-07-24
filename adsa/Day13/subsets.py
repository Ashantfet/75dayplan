class Solution:
    def func(self,index,subset,nums: list[int],result):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.func(index+1,subset,nums,result)
        subset.pop()
        self.func(index+1,subset,nums,result)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset =[]
        self.func(0,subset,nums,result)
        return result

nums = list(map(int, input().split()))
sol = Solution()
print(sol.subsets(nums))