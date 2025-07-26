class Solution:
    def solve(self,digits,char_map,result,index,subset):
        if len(digits)==0:
            return
        if index == len(digits):
            result.append("".join(subset))
            return
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.solve(digits,char_map,result,index+1,subset)
            subset.pop()
    def letterCombinations(self, digits: str) -> list[str]:
        result =[]
        char_map = {
            "2": "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7": "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        self.solve(digits,char_map,result,0,[])
        return result

n = input().strip()
sol = Solution()
result = sol.letterCombinations(n)
for combination in result:
    print(combination, end=" ")