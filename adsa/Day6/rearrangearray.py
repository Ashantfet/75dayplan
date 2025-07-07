class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        
        return result
nums = list(map(int, input().split()))
sol = Solution().rearrangeArray(nums)
print(*sol)