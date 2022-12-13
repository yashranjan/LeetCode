class Solution:
    def dfs(self, curr, visited, adj_lst):
        visited[curr] = True
        for conn in adj_lst[curr]:
            if not visited[conn]:
                self.dfs(conn, visited, adj_lst)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_lst = [[] for i in range(n)]
        
        for i,j in edges:
            adj_lst[i].append(j)
            adj_lst[j].append(i)
        
        visited = [False]*n
        
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                self.dfs(i, visited, adj_lst)
        
        return ans