class Solution:
    def findFrequency(self, arr, x):
        h_map = {}
        for i in arr:
            h_map[i] = h_map.get(i, 0) + 1
        
        return h_map.get(x, 0)
x = list(map(int, input().split()))
y = int(input())
ob = Solution()
print(ob.findFrequency(x, y))