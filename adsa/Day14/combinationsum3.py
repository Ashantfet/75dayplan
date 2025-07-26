class Solution:
    def solve(self,index,k,n,subset,result):
        if n==0 and len(subset) ==k:
            result.append(subset.copy())
            return
        if n<0 or len(subset) >k:
            return
        for i in range(index,10):
            subset.append(i)
            self.solve(i+1,k,n-i,subset,result)
            subset.pop()
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        self.solve(1,k,n,[],result)
        return result
n = int(input())  ## Input the target sum
k = int(input()) ## Input the number of elements in the combination
sol = Solution()
result = sol.combinationSum3(k, n)
for combination in result:
    print(combination, end=" ")