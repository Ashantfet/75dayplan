class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        n=len(arr)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if arr[j] >arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    
arr = list(map(int, input().split()))
sol = Solution()
sol.bubbleSort(arr)
print(*arr)