
class Solution:
    # def backtrack(self,index,total,subset,result,arr,k):
    #     if total==k:
    #         result.append(subset.copy())
    #         return True
    #     elif total >k:
    #         return False
    #     if index>=len(arr):
    #         return False
    #     subset.append(arr[index])
    #     sum= total+arr[index]
    #     pick = self.backtrack(index+1,sum,subset,result,arr,k)
    #     if pick==True:
    #         return True
    #     e= subset.pop()
    #     sum = total
    #     notpick = self.backtrack(index+1,sum,subset,result,arr,k)
    #     return notpick
    def backtrack(self, index, total, subset, result, arr, k):
        if total == k:
            result.append(subset.copy())
            return True
        elif total > k or index >= len(arr):
            return False

        # Include the current element
        subset.append(arr[index])
        if self.backtrack(index + 1, total + arr[index], subset, result, arr, k):
            return True
        subset.pop()

        # Exclude the current element
        if self.backtrack(index + 1, total, subset, result, arr, k):
            return True

        return False
    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        result =[]
        subset =[]
        return self.backtrack(0,0,subset,result,arr,K)

N = int(input())
arr = list(map(int, input().split()))
K = int(input())
sol = Solution()
print(sol.checkSubsequenceSum(N, arr, K))