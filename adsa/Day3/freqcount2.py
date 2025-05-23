class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        h_map = {}
        result = []

        for i in arr:
            if 1 <= i <= n:
                h_map[i] = h_map.get(i, 0) + 1
        for i in range(1, n + 1):
            result.append(h_map.get(i, 0))

        return result
x = list(map(int, input().split()))
ob = Solution()
print(*ob.frequencyCount(x))