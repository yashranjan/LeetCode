class Solution:
    def make_graph(self, stones):
        graph = dict()
        for x,y in stones:
            if (x, y) not in graph:
                graph[(x, y)] = []
            keys = graph.keys()
            for k_x, k_y in keys:
                if k_x==x or k_y==y:
                    graph[(k_x, k_y)].append((x, y))
                    graph[(x, y)].append((k_x, k_y))
            
        return graph
    
    def dfs(self, coord, graph, visited) -> None:
        visited.add(coord)
        for v_coord in graph[coord]:
            if v_coord in visited:
                continue
            self.dfs(v_coord, graph, visited)
    
    def conn_comps(self, graph) -> int:
        cnt = 0
        visited = set()
        for k_x, k_y in graph.keys():
            if (k_x, k_y) in visited:
                continue
            cnt += 1
            self.dfs((k_x, k_y), graph, visited)
        
        return cnt
        
    
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = self.make_graph(stones)
        return len(stones)-self.conn_comps(graph)