class Solution:    
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()
        
        platform_needed = 1
        max_platforms = 1
        
        i = 1  
        j = 0  
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            else:
                platform_needed -= 1
                j += 1
            max_platforms = max(max_platforms, platform_needed)
        
        return max_platforms
arr = list(map(int, input().split()))
dep = list(map(int, input().split()))
solution = Solution()
print(solution.minimumPlatform(arr, dep))