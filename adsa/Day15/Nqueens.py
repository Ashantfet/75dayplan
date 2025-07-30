class Solution:
    def issafe(self,row,col,board,n):
        duprow = row
        dupcol = col
        while row >=0 and col >=0:
            if board [row][col] == "Q":
                return False
            row -=1
            col -=1

        col = dupcol
        row = duprow
        while col >=0:
            if board[row][col] =="Q":
                return False
            col -=1

        row =duprow
        col = dupcol
        while row <n and col >= 0:
            if board[row][col] == "Q":
                return False
            row+=1
            col-=1
        
        return True
    def solve(self,col,board,ans,n):
        if col ==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.issafe(row,col,board,n):
                board[row] =board[row][:col]+"Q"+board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row] = board[row][:col]+"."+board[row][col+1:]
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = ["." * n for _ in range(n)]
        ans=[]
        self.solve(0,board,ans,n)
        return ans
    
n= int(input())  ## Input the size of the chessboard
sol = Solution()
result = sol.solveNQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()  # Print a newline between different solutions