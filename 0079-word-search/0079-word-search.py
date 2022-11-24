class Solution:
    def solve(self, board, m, n, x, y, word, idx):
        if idx==len(word):
            return True
        
        curr = board[x][y]
        board[x][y] = '-'
        for d_x, d_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n_x, n_y = x+d_x, y+d_y
            if n_x>=0 and n_x<m and n_y>=0 and n_y<n and word[idx]==board[n_x][n_y]:
                if self.solve(board, m, n, n_x, n_y, word, idx+1):
                    return True
        board[x][y] = curr
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if self.solve(board, m, n, i, j, word, 1):
                        return True
        return False