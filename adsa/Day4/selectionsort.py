class Solution: 
    def selectionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(0,n):
            mini = i
            for j in range(i+1,n):
                if arr[j] < arr[mini] :
                    mini =j
            arr[i],arr[mini] =arr[mini],arr[i]

arr = list(map(int, input().split()))
sol = Solution()
sol.selectionSort(arr)
print(*arr)
