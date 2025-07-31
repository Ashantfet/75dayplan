#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        stack = []
        n = len(pre_exp)
        for i in range(n-1,-1,-1):
            char =pre_exp[i]
            if char.isalnum():
                stack.append(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                new_exp = op1+op2+char
                stack.append(new_exp)
        return stack[-1]
s = input()  
solution = Solution()
print(solution.preToPost(s))