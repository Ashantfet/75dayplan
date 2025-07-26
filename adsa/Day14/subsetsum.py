class Solution:
    def solve(self, arr, index,total,result):
        if index >=len(arr):
            result.append(total)
            return 
        sum = total +arr[index]
        self.solve(arr,index+1,total+arr[index],result)
        sum = total
        self.solve(arr,index+1,total,result)
    def subsetSums(self, arr):
		# code here
        result =[]
        self.solve(arr,0,0,result)
        return result

arr = list(map(int, input().split()))
sol = Solution()
result = sol.subsetSums(arr)
for sum in result:
    print(sum, end=" ")