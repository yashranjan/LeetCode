class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        
        currRow = currCol = 0
        while currRow < (n+1)//2:
            currCol = 0
            while currCol < (m)//2:
                fourLocs = [(currRow, currCol), (currCol, n-1-currRow), (n-1-currRow, m-1-currCol), (m-1-currCol, currRow)]
                fourVals = [matrix[fourLocs[-1][0]][fourLocs[-1][1]]] + [matrix[i][j] for i,j in fourLocs[:-1]]
                for (x,y),val in zip(fourLocs, fourVals):
                    matrix[x][y] = val
                currCol += 1
            currRow += 1
            