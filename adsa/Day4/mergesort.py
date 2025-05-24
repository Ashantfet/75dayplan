class Solution:
    def merge(self, arr, l, r):
        m = (l + r) // 2
        # Create temporary arrays
        left = arr[l:m+1]
        right = arr[m+1:r+1]

        i = j = 0
        k = l

        # Merge left and right into original array
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, r) 

arr = list(map(int, input().split()))
l=0
r=len(arr)-1
sol = Solution()
sol.mergeSort(arr,l,r)
print(*arr)