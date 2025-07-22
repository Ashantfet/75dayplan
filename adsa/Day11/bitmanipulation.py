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
    def con2deci(self, binary):
        ans = 0
        for i, bit in enumerate(binary[::-1]):
            ans += int(bit) * (2 ** i)
        return ans
        
    def geti(self,binary, i):
        if i > len(binary):
            return 0
        return int(binary[-i]) 
    def seti (self,binary,i):
        binary = list(binary.zfill(i)) 
        if binary[-i] =="0":
            binary[-i] = "1"
        return self.con2deci("".join(binary))
    def cleari(self,binary,i):
        binary = list(binary.zfill(i))
        if binary[-i] == "1":
            binary[-i] ="0"
        return self.con2deci("".join(binary))
    def bitManipulation(self, num, i):
        # Code here
        binary = self.con2bin(num)
        getibit = self.geti(binary,i)
        setibit = self.seti(binary,i)
        clearibit = self.cleari(binary,i)
        print(getibit, setibit, clearibit)
num = int(input())
i = int(input())
sol = Solution()
sol.bitManipulation(num, i)