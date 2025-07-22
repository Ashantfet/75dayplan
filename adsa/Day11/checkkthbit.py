class Solution:
    def con2bin(self,num):
        result = ""
        while(num>0):
            if num%2 ==0:
                result +="0"
            else:
                result +="1"
            num = num//2
        result = result[ : :-1]
        return result
    def checkKthBit(self, n, k):
        # code here
        binary = self.con2bin(n)
        if k >= len(binary):
            return False
        return binary[-k-1] == "1"

n= int(input())
k = int(input())
sol = Solution()
print(sol.checkKthBit(n, k))