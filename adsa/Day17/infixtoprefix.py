class Solution:
    def precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == '^':
            return 3
        return 0

    def infixToPrefix(self, s):
        # Step 1: Reverse the infix string and swap parentheses
        s = s[::-1]
        s = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in s])
        
        stack = []
        result = []

        # Step 2: Convert to postfix
        for char in s:
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                if stack: stack.pop()
            else:  # operator
                while (stack and
                       ((self.precedence(stack[-1]) > self.precedence(char)) or
                        (self.precedence(stack[-1]) == self.precedence(char) and char != '^'))):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        # Step 3: Reverse postfix to get prefix
        return ''.join(result[::-1])
s = input()
solution = Solution()
print(solution.infixToPrefix(s))