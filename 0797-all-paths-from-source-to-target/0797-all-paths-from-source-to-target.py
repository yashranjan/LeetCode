class Solution:
    def solve(self, graph, curr, et, res):

        if curr == et:
            return res[:]
        ans = []
        for j in graph[curr]:
            res.append(j)
            tmp = self.solve(graph, j, et, res)
            if not tmp:
                res.pop()
                continue
            if type(tmp[0]) == type([]):
                ans.extend(tmp)
            else:
                ans.append(tmp)
            res.pop()
    
        return ans
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = [0]
        return self.solve(graph, 0, len(graph)-1, ans)