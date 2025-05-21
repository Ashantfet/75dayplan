class Solution:
    def factor(self, n: int) -> list[int]:
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return sorted(factors)

x=int(input())
sol=Solution()
print(sol.factor(x))

# class Solution2:
#     def factor(self, n: int) -> list[int]:
#         factors = []
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 factors.append(i)
#         return factors
# x=int(input())
# sol=Solution2()
# print(sol.factor(x))

# class Solution3:
#     def factor(self, n: int) -> list[int]:
#         factors = []
#         for i in range(1, (n//2)+1):
#             if n % i == 0:
#                 factors.append(i)
#         factors.append(n)
#         return factors
# x=int(input())
# sol=Solution3()
# print(sol.factor(x))