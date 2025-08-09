
class Solution:
    def count(self, n):
        # Code here
        if n==1 or n==2:
            return n
        edges = n*(n-1)//2
        return 2**edges
n = int(input())
sol = Solution()
print(sol.count(n))  # Output: number of ways to connect n nodes with edges
# Example: For n=3, the output should be 8 (2^(3*(3-1)/2) = 2^3 = 8)