class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        ans = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) !=0:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans

s = input()
solution = Solution()
arr = list(map(int, s.split()))
print(*solution.nextLargerElement(arr))