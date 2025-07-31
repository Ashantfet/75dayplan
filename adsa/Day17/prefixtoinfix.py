#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for char in pre_exp[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_exp = f"({operand1}{char}{operand2})"
                stack.append(new_exp)
                
        return stack[-1]
s = input()
solution = Solution()
print(solution.preToInfix(s))