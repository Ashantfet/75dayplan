class Solution:
    def countSetBits(self,n):
        total = 0
        i = 0
        while (1 << i) <= n:
            # Number of full cycles of length 2^(i+1)
            full_cycles = (n + 1) // (1 << (i + 1))
            # Each full cycle contributes 2^i set bits at position i
            total += full_cycles * (1 << i)
    
            # Remainder part after full cycles
            remainder = (n + 1) % (1 << (i + 1))
            extra = max(0, remainder - (1 << i))
            total += extra
    
            i += 1
        return total
n = int(input())
sol = Solution()
print(sol.countSetBits(n))