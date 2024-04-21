class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjLst = [[] for _ in range(n)]
        for (s, e) in edges:
            adjLst[s].append(e)
            adjLst[e].append(s)
        
        stk = [source]
        while stk:
            curr = stk.pop()
            visited.add(curr)
            if curr == destination:
                return True
            for dst in adjLst[curr]:
                if dst not in visited:
                    stk.append(dst)
        return False            