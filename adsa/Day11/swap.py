class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        a=a^b
        b=a^b
        a=a^b
        return [a,b]

n1, n2 = map(int, input().split())
sol = Solution()
print(*sol.get(n1, n2))  