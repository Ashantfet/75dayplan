# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(1,n):
            key =arr[i]
            j=i-1
            while(j>=0 and arr[j]>key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1] = key

arr = list(map(int, input().split()))
sol = Solution()
sol.insertionSort(arr)
print(*arr)