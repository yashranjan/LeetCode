class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totIslands = 0
        n, m = len(grid), len(grid[0])
        isVisited = [[False]*m for i in range(n)]
        xyDir = [(-1,0), (0, -1), (0, 1), (1, 0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not isVisited[i][j]:
                    totIslands += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        isVisited[x][y] = True
                        for xDir, yDir in xyDir:
                            currX, currY = x+xDir, y+yDir
                            if currX>=0 and currY>=0 and currX<n and currY<m and not isVisited[currX][currY] and grid[currX][currY]=='1':
                                stack.append((currX, currY))

        return totIslands
                    
                