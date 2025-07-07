class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row0 = col0 = False

        # 1. Check if first row and column need to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(cols):
            if matrix[0][j] == 0:
                row0 = True

        # 2. Use first row/column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. Set matrix cells to zero using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. Zero first row and column if needed
        if col0:
            for i in range(rows):
                matrix[i][0] = 0
        if row0:
            for j in range(cols):
                matrix[0][j] = 0
# Example usage
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
Solution().setZeroes(matrix)
for row in matrix:
    print(row)