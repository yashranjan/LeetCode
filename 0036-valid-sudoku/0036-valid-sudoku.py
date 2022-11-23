class Solution:
    def isValid(self, board, x, y, n=9):
        
        fnd = set()
        for i in board[x]:
            if i!='.' and i in fnd:
                return False
            fnd.add(i)
        fnd.clear()
        for i in range(n):
            if board[i][y]!='.' and board[i][y] in fnd:
                return False
            fnd.add(board[i][y])
        maxX = x//3 + (2*(x//3))
        maxY = y//3 + (2*(y//3))
        fnd.clear()
        print(x, y, maxX, maxX+3, maxY, maxY+3)
        for i in range(maxX, maxX+3):
            for j in range(maxY, maxY+3):
                print(board[i][j], end=' ')
                if board[i][j]!='.' and board[i][j] in fnd:
                    return False
                fnd.add(board[i][j])
        print()
        return True
            
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        
        
        for i in range(n):
            for j in range(n):
                if board[i][j]!='.' and not self.isValid(board, i, j):
                    return False
        
        return True