class Solution:
    def dfs(self, grid, x, y, isVisited, n, m):
        xyDir = [(-1,0), (0, -1), (0, 1), (1, 0)]
        isVisited[x][y] = True
        for i,j in xyDir:
            currX, currY = x+i, y+j
            if currX>=0 and currY>=0 and currX<n and currY<m and not isVisited[currX][currY] and grid[currX][currY]=='1':
                self.dfs(grid, currX, currY, isVisited, n, m)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        totIslands = 0
        n, m = len(grid), len(grid[0])
        isVisited = [[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not isVisited[i][j]:
                    totIslands += 1
                    self.dfs(grid, i, j, isVisited, n, m)

        return totIslands
                    
                