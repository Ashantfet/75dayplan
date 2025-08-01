class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            # Process current asteroid
            while stack and a < 0 < stack[-1]:
                # If top is smaller than current, it explodes
                if stack[-1] < -a:
                    stack.pop()
                    continue
                # If equal, both explode
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                # No collision, add to stack
                stack.append(a)
        return stack
nums = list(map(int, input().split()))
solution = Solution()
print(*solution.asteroidCollision(nums))