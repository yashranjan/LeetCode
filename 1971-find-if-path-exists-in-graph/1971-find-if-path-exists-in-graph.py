class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjLst = [[] for _ in range(n)]
        for (s, e) in edges:
            adjLst[s].append(e)
            adjLst[e].append(s)
        
        q = [source]
        qIdx = 0
        while qIdx<len(q):
            curr = q[qIdx]
            qIdx += 1
            visited.add(curr)
            if curr == destination:
                return True
            for dst in adjLst[curr]:
                if dst not in visited:
                    q.append(dst)
        return False            