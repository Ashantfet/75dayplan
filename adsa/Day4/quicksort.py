class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            # Move right until an element >= pivot is found
            i += 1
            while arr[i] < pivot:
                i += 1

            # Move left until an element <= pivot is found
            j -= 1
            while arr[j] > pivot:
                j -= 1

            # If pointers have crossed, return j
            if i >= j:
                return j

            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]

    def quickSort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p)
            self.quickSort(arr, p + 1, high)

arr = list(map(int, input().split()))
l=0
r=len(arr)-1
sol = Solution()
sol.quickSort(arr,l,r)
print(*arr)