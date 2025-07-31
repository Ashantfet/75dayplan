#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack = []
        for char in post_exp:
            if char.isalnum():
                stack.append(char)
            else:
                op1 =stack.pop()
                op2 =stack.pop()
                new_exp =char+op2+op1
                stack.append(new_exp)
        return stack[-1]
s = input()
solution = Solution()
print(solution.postToPre(s))