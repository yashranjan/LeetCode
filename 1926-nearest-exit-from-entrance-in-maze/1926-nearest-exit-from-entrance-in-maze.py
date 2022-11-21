class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        x, y = entrance[0], entrance[1]
        maze[x][y] = '+'
        
        queue = collections.deque()
        queue.append([x, y, 0])
        
        while queue:
            curr_x, curr_y, curr_d = queue.popleft()
            for d_x, d_y in dirs:
                new_x, new_y = curr_x+d_x, curr_y+d_y
                if new_x>=0 and new_y>=0 and new_x<m and new_y<n and maze[new_x][new_y]=='.':
                    if new_x==0 or new_y==0 or new_x==m-1 or new_y==n-1:
                        return curr_d+1
                    maze[new_x][new_y] = '+'
                    queue.append([new_x, new_y, 1+curr_d])
        
        return -1