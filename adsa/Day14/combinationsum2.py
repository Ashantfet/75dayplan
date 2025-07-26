class Solution:
    def solve(self,index,total,subset,result,nums):
        n= len(nums)
        if total ==0:
            result.append(subset.copy())
            return
        if index >=len(nums) or total <0:
            return
        for i in range(index,n):
            if i >index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.solve(i+1,total-nums[i],subset,result,nums)
            subset.pop()
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.solve(0,target,[],result,candidates)
        return result 
n = int(input())
candidates = list(map(int, input().split()))
sol = Solution()
result = sol.combinationSum2(candidates, n)
for combination in result:
    print(combination, end=" ")