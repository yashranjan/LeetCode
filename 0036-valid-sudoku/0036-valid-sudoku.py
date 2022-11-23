class Solution:
    def isValid(self, board, x, y, n=9):
        
        fnd = set()
        maxX = x//3 + (2*(x//3))
        maxY = y//3 + (2*(y//3))
        for i in range(maxX, maxX+3):
            for j in range(maxY, maxY+3):
                if board[i][j]!='.' and board[i][j] in fnd:
                    return False
                fnd.add(board[i][j])

        return True
            
    def isValidRow(self, board, row, n=9):
        fnd = set()
        for i in range(n):
            if board[row][i]!='.' and board[row][i] in fnd:
                return False
            fnd.add(board[row][i])
        return True
    
    def isValidCol(self, board, col, n=9):
        fnd = set()
        for i in range(n):
            if board[i][col]!='.' and board[i][col] in fnd:
                return False
            fnd.add(board[i][col])
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        
        for i in range(n):
            if not self.isValidRow(board, i):
                return False
        
        for i in range(n):
            if not self.isValidCol(board, i):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValid(board, i, j):
                    return False
        
        return True