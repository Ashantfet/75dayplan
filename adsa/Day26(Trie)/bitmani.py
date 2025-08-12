
class Solution:
    def XOR(self, n, m):
        return n ^ m

    def check(self, a, b):
        return 1 if (b & (1 << (a - 1))) != 0 else 0

    def setBit(self, c, d):
        return d | (1 << c)

n,m= map(int, input().strip().split())
a,b= map(int, input().strip().split())
c,d = map(int, input().strip().split())

sol = Solution()
print(sol.XOR(n, m))  # Output: XOR of n and m
print(sol.check(a, b))  # Output: 1 if bit a is set in b, else 0
print(sol.setBit(c, d))  # Output: d with bit c set