class Solution:
    def solve(self,open_count,close_count,brackets,result,n):
        if len(brackets) == 2*n:
            result.append("".join(brackets))
            return
        if open_count <n:
            brackets.append("(")
            self.solve(open_count+1,close_count,brackets,result,n)
            brackets.pop()
        if close_count <open_count:
            brackets.append(")")
            self.solve(open_count,close_count+1,brackets,result,n)
            brackets.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        
        result =[]
        self.solve(0,0,[],result,n)
        return result

n = int(input())
sol = Solution()
result = sol.generateParenthesis(n)
for parenthesis in result:
    print(parenthesis, end=" ")