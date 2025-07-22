class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        length = 1<<n
        result = []
        for i in range(0,length):
            lst = []
            for j in range(0,n):
                if (i & (1<<j)) != 0 :
                    lst.append(nums[j])
            result.append(lst)
        return result
nums = list(map(int, input().split()))
sol = Solution()
print(sol.subsets(nums))