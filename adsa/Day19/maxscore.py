class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        max_score = total
        for i in range(1, k + 1):
            total -= cardPoints[k - i]       
            total += cardPoints[-i]          
            max_score = max(max_score, total)

        return max_score

cardPoints = list(map(int, input().split()))
k = int(input())
solution = Solution()
print(solution.maxScore(cardPoints, k))