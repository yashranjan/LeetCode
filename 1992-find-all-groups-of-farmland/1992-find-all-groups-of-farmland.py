class Solution:
    diff_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def findMax(self, land, curr_x, curr_y, n, m):
        land[curr_x][curr_y] = -1
        max_x, max_y = curr_x, curr_y
        for d_x, d_y in self.diff_coords:
            n_x, n_y = curr_x+d_x, curr_y+d_y
            if n_x>=0 and n_y>=0 and n_x<n and n_y<m and land[n_x][n_y] == 1:
                poss_x, poss_y = self.findMax(land, n_x, n_y, n, m)
                max_x = max(max_x, poss_x)
                max_y = max(max_y, poss_y)
        
        return (max_x, max_y)
        
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n, m = len(land), len(land[0])
        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    coords = self.findMax(land, i, j, n, m)
                    ans.append([i, j, coords[0], coords[1]])
        
        return ans