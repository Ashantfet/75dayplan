#User function Template for python3

class Solution:
    def solve(self,index,flag,numbers,result,n):
        if index == n:
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.solve(index+1,True,numbers,result,n)
        if flag ==True:
            numbers[index]="1"
            self.solve(index+1,False,numbers,result,n)
            numbers[index]="0"
            
    def generateBinaryStrings(self, n):
        # Code here
        numbers = ["0"]*n
        result = []
        self.solve(0,True,numbers,result,n)
        return result

n= int(input())
sol = Solution()
result = sol.generateBinaryStrings(n)
for binary_string in result:
    print(binary_string, end=" ")