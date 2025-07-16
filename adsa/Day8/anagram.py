class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=sorted(s)
        y=sorted(t)
        if x==y:
            return True
        else:
            return False
s = input()
t = input()
sol = Solution()
result = sol.isAnagram(s, t)
print(result)