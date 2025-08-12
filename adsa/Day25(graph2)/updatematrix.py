from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visited =[[0 for _ in range(cols)] for _ in range(rows)]
        distance =[[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    visited[r][c] =1
        while len(queue) !=0:
            i,j,d = queue.popleft()
            distance[i][j] = d
            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_i ,new_j = i+x, j+y
                if new_i <0 or new_i >=rows or new_j <0 or new_j >= cols or visited[new_i][new_j] ==1:
                    continue
                queue.append([new_i,new_j,d+1])
                visited[new_i][new_j]=1
        return distance

mat = []
rows = int(input())
for _ in range(rows):
    row = list(map(int, input().split()))
    mat.append(row)
sol = Solution()
result = sol.updateMatrix(mat)
for row in result:
    print(" ".join(map(str, row)))

# Output: The updated matrix with distances from the nearest 0