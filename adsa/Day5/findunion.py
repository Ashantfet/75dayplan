#User function Template for python3

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        
        n = len(a)-1
        m = len(b)-1
        i=0
        j=0
        temp = []
        
        while(j<=m and i<=n):
            if(a[i] <= b[j]):
                temp.append(a[i])
                i+=1
            else:
                temp.append(b[j])
                j+=1
        while(j<=m):
            temp.append(b[j])
            j+=1
        while(i<=n):
            temp.append(a[i])
            i+=1
        r = self.removeDuplicates(temp)
        return temp[:r]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
sol = Solution()
x = sol.findUnion(a, b)
print(x)  # Print the union of the two arrays