class Solution:
    def findFloor(self, arr, x):
        if x < arr[0]:
            return -1

        l = 0
        r = len(arr) - 1
        floor_index = -1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                floor_index = mid
                l = mid + 1
            else:
                r = mid - 1

        return floor_index
arr = list(map(int, input().split()))
x = int(input())
sol = Solution().findFloor(arr, x)
print(sol)