#User function Template for python3

class Solution:
    def xor_upto(self,n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0
    def findXOR(self, l, r):
        # Code here
        return self.xor_upto(r) ^ self.xor_upto(l - 1)
l, r = map(int, input().split())
sol = Solution()
print(sol.findXOR(l, r))