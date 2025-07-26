class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total == target:
            result.append(subset.copy())
            return
        elif target < total or index >= len(nums):
            return
        subset.append(nums[index])
        self.solve(index,total+nums[index],subset,nums,target,result)
        subset.pop()
        self.solve(index+1,total,subset,nums,target,result)
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result =[]
        self.solve(0,0,[],candidates,target,result)
        return result

n = int(input())
candidates = list(map(int, input().split()))
sol = Solution()
result = sol.combinationSum(candidates, n)
for combination in result:
    print(combination, end=" ")