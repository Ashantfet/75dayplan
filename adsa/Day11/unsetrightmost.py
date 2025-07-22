#User function Template for python3
class Solution:
	def setBit(self, n):
		# code here
		ans = n | (n+1)
		return ans
n = int(input())
sol = Solution()
print(sol.setBit(n))