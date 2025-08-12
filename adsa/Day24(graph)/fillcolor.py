import collections
from typing import List
from copy import deepcopy
from collections import deque
# class Solution:
#     def dfs(self,i,j,new_color,ini_color,r,c,vis):
#         if i <0 or i>=r or j<0 or j>=c or vis[i][j] ==new_color or vis[i][j]!= ini_color:
#             return 
#         vis[i][j] = new_color
#         self.dfs(i+1,j,new_color,ini_color,r,c,vis)
#         self.dfs(i,j+1,new_color,ini_color,r,c,vis)
#         self.dfs(i-1,j,new_color,ini_color,r,c,vis)
#         self.dfs(i,j-1,new_color,ini_color,r,c,vis)
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if image[sr][sc] == color:
#             return image
#         visited = deepcopy(image)
#         rows= len(visited)
#         cols= len(visited[0])
#         initialcolor= visited[sr][sc]
        
#         self.dfs(sr,sc,color,initialcolor,rows,cols,visited)
#         return visited
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visited = deepcopy(image)
        rows= len(visited)
        cols= len(visited[0])
        initialcolor= visited[sr][sc]
        queue=deque()
        queue.append((sr,sc))

        while len(queue)!=0:
            i,j =queue.popleft()
            visited[i][j] =color
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i =i+x
                new_j =j+y
                if new_i <0 or new_i >=rows or new_j <0 or new_j >= cols:
                    continue
                if visited[new_i][new_j] != initialcolor:
                    continue
                queue.append((new_i,new_j))
        return visited
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol = Solution()
print(sol.floodFill(image, sr, sc, color))  # Output: [[2,2,2],[2,2,0],[2,0,1]]