class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n= len(nums)
        maxi =0
        right =0
        left =0
        zeros =0
        while right <n:
            if nums[right]==0:
                zeros +=1
            if zeros >k:
                if nums[left]==0:
                    zeros -=1
                left+=1
            if zeros <=k:
                maxi = max(maxi,right-left+1)
            right +=1
        return maxi
s= list(map(int, input().split()))
k = int(input())
solution = Solution()
print(solution.longestOnes(s, k))