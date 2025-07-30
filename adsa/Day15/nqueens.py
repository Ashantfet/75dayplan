class Solution:
    def solve(self,col,board,ans,leftrow,upperdiagonal,lowerdiagonal,n):
        if col ==n:
            ans.append(board[:])
            return
        for row in range(n):
            if(
                leftrow[row] ==0 
                and lowerdiagonal[row+col]  ==0
                and upperdiagonal[n-1 +col -row] ==0):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                leftrow[row]=1
                lowerdiagonal[row+col] =1
                upperdiagonal[n-1+col-row] =1
                self.solve(col+1,board,ans,leftrow,upperdiagonal,lowerdiagonal,n)
                board[row] = board[row][:col] + "." + board[row][col+1:]
                leftrow[row] =0
                lowerdiagonal[row+col] =0
                upperdiagonal[n-1+col-row] =0

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = ["." * n for _ in range(n)]
        ans=[]
        leftrow=[0]*n
        upperdiagonal =[0]*(2*n-1)
        lowerdiagonal = [0]*(2*n-1)
        self.solve(0,board,ans,leftrow,upperdiagonal,lowerdiagonal,n)
        return ans
n = int(input())  ## Input the size of the chessboard
sol = Solution()
result = sol.solveNQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()  # Print a newline between different solutions