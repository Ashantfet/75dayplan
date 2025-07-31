#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack =[]
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            else:
                op1 =stack.pop()
                op2 =stack.pop()
                new_exp ="("+op2+char+op1+")"
                stack.append(new_exp)
        return stack[-1]
s = input()
solution = Solution()
print(solution.postToInfix(s))