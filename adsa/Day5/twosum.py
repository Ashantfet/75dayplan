class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i

arr = list(map(int, input().split()))
target = int(input())
sol = Solution().twoSum(arr, target)
print(*sol)