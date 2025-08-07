#User function Template for python3

class Solution:
    def countNodes(self, i):
        # Code here
        return 2**(i-1)

i= int(input())
solution = Solution()
print(solution.countNodes(i))