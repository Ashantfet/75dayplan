class Solution:
    
    def maximumMeetings(self, start, end):
        n = len(start)
        meetings = [(start[i], end[i], i + 1) for i in range(n)]
        
        meetings.sort(key=lambda x: x[1])
        
        result = [meetings[0][2]]  
        last_end_time = meetings[0][1]
        count = 1
        
        for i in range(1, n):
            if meetings[i][0] > last_end_time:
                result.append(meetings[i][2])
                last_end_time = meetings[i][1]
                count += 1
        
        return count
start = list(map(int, input().split()))
end = list(map(int, input().split()))
solution = Solution()
print(solution.maximumMeetings(start, end))