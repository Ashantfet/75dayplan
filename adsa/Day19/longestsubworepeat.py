# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n= len(s)
#         maxi =0
#         for i in range(0,n):
#             my_set = set()
#             for j in range(i,n):
#                 if s[j] in my_set:
#                     break
#                 maxi = max(maxi,j-i+1)
#                 my_set.add(s[j])
#         return maxi

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        maxi =0
        left =0
        right =0
        my_dict = {}
        while(right<n):
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            maxi = max(maxi,right-left+1)
            my_dict[s[right]] = right
            right+=1
        return maxi
s = input()
solution = Solution()
print(solution.lengthOfLongestSubstring(s))