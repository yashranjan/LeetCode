class Solution:
    diff_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]        
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n, m = len(land), len(land[0])
        
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    stk = [(i, j)]
                    max_x, max_y = i, j
                    while stk:
                        curr_x, curr_y = stk.pop()
                        land[curr_x][curr_y] = -1
                        max_x = max(max_x, curr_x)
                        max_y = max(max_y, curr_y)
                        for d_x, d_y in self.diff_coords:
                            n_x, n_y = curr_x+d_x, curr_y+d_y
                            if n_x>=0 and n_y>=0 and n_x<n and n_y<m and land[n_x][n_y] == 1:
                                stk.append((n_x, n_y))
                    
                    ans.append([i, j, max_x, max_y])
        return ans