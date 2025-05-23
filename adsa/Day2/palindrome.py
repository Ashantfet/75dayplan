# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
        
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
            
#         return True

class Solution:
    def palin(self,s,l,r):
        if l >=r:
            return True
        if s[l] != s[r]:
            return False
        return self.palin(s,l+1,r-1)
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        
        y=self.palin(s,left,right)
        return y
x = input()
ob = Solution()
print(ob.isPalindrome(x))