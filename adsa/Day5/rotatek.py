class Solution:
    def reverse(self,nums:list[int],left,right):
        while (left<right):
            nums[left],  nums[right] =nums[right],nums[left]
            left +=1
            right -=1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)

nums = list(map(int, input().split()))
k= int(input())
sol = Solution()
x = sol.rotate(nums,k)
print(nums)