class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
arr = list(map(int, input().split()))
x = int(input())
sol = Solution()
result = sol.search(arr, x)
print(result)   