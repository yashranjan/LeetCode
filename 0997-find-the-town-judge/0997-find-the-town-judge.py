class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        isJudge = [0]*(n+1)
        for i,j in trust:
            isJudge[i]-=1
            isJudge[j]+=1
        
        for judge in range(1, n+1):
            if isJudge[judge]==n-1:
                return judge
        return -1