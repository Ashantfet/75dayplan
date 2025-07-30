class Solution:
    # Function to find all possible paths
    def findpathhelper(self,i,j,a,n,ans,move,vis):
        if i ==n-1 and j ==n-1:
            ans.append(move)
            return
        vis[i][j] = 1

        #downward
        if i+1 <n and not vis[i+1][j] and a[i+1][j]==1:
            # vis[i][j] = 1
            self.findpathhelper(i+1,j,a,n,ans,move+"D",vis)
            # vis[i][j] = 0
        
        if j-1 >= 0 and not vis[i][j-1] and a[i][j-1]==1:
            # vis[i][j] = 1
            self.findpathhelper(i,j-1,a,n,ans,move+"L",vis)
            # vis[i][j] = 0
        
        if j+1 <n and not vis[i][j+1] and a[i][j+1]==1:
            # vis[i][j] = 1
            self.findpathhelper(i,j+1,a,n,ans,move+"R",vis)
            # vis[i][j] = 0
                
        if i-1 >=0 and not vis[i-1][j] and a[i-1][j]==1:
            # vis[i][j] = 1
            self.findpathhelper(i-1,j,a,n,ans,move+"U",vis)
            # vis[i][j] = 0
        vis[i][j] = 0

    def ratInMaze(self, maze):
        # code here
        n=len(maze)
        ans= []
        vis =[[0 for _ in range(n)]for _ in range(n)]
        if maze[0][0] ==1:
            self.findpathhelper(0,0,maze,n,ans,"",vis)
        return ans
n= int(input())  # Input the size of the maze
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
sol = Solution()
result = sol.ratInMaze(maze)
for path in result:
    print(path)