class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(a):
            if parents[a] == a:
                return a
            parents[a] = find(parents[a])
            return parents[a]
        
        def union(a, b):
            a = find(a)
            b = find(b)
            parents[b] = a
        
        parents = [i for i in range(n)]
        logs.sort(key = lambda x: x[0])
        ans = -1
        for log in logs:
            a, b= log[1], log[2]
            union(a, b)
            if len([i for i in range(n) if i==parents[i]]) == 1:
                ans = log[0]
                break

        return ans