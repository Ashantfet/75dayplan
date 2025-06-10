class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i

arr = list(map(int, input().split()))
target = int(input())
sol = Solution().twoSum(arr, target)
print(*sol)