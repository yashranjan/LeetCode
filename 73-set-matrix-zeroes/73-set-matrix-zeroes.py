class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        
        isRowZero, isColZero = [False]*n, [False]*m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    isRowZero[i] = isColZero[j] = True
        
        for i in range(n):
            for j in range(m):
                if isRowZero[i] or isColZero[j]:
                    matrix[i][j] = 0