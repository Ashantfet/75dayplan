# #User function Template for python3
# class Solution:
#     def distsubseq(self,s: str) -> set:
#         result = set()

#         def dfs(index: int, path: str):
#             if index == len(s):
#                 if path:
#                     result.add(path)
#                 return
#             # Choice 1: Include current character
#             dfs(index + 1, path + s[index])
#             # Choice 2: Exclude current character
#             dfs(index + 1, path)
    
#         dfs(0, "")
#         return result

#     def betterString(self, s1, s2):
#         # Code here
#         a= self.distsubseq(s1)
#         b=self.distsubseq(s2)
#         return s1 if len(a) >=len(b) else s2

class Solution:
    def countDistinctSubseq(self, s: str) -> int:
        MOD = 10**9 + 7  
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty subsequence

        last_occurrence = {}
        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = 2 * dp[i - 1]

            if char in last_occurrence:
                dp[i] -= dp[last_occurrence[char] - 1]

            last_occurrence[char] = i

        return dp[n] - 1  # Subtract empty subsequence

    def betterString(self, s1: str, s2: str) -> str:
        count1 = self.countDistinctSubseq(s1)
        count2 = self.countDistinctSubseq(s2)
        return s1 if count1 >= count2 else s2

s1 = input().strip()
s2 = input().strip()
sol = Solution()
result = sol.betterString(s1, s2)
print(result)