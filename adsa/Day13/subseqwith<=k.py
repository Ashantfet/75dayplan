class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        
        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % mod

        ans = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow2[right - left]) % mod
                left += 1
            else:
                right -= 1

        return ans

nums = list(map(int, input().split()))
target = int(input())
sol = Solution()
print(sol.numSubseq(nums, target))