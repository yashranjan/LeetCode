class Solution:
    def fillLand(self, grid, i, j, n, m):
        grid[i][j] = '-'
        for d_x, d_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_x, n_y = i+d_x, j+d_y
            if n_x>=0 and n_y>=0 and n_x<n and n_y<m and grid[n_x][n_y]=='1':
                self.fillLand(grid, n_x, n_y, n, m)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    self.fillLand(grid, i, j, n, m)
        return cnt