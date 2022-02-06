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
            if a==b: return False
            parents[b] = a
            return True
        
        parents = [i for i in range(n)]
        logs.sort(key = lambda x: x[0])
        ans = -1
        grpCnt = n
        for log in logs:
            a, b= log[1], log[2]
            if union(a, b):
                grpCnt -= 1
            if grpCnt == 1:
                ans = log[0]
                break

        return ans