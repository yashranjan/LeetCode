class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        isJudge = dict()
        for i in range(1,n+1):
            isJudge[i] = []
        trustCnt = [0]*(n+1)

        for i,j in trust:
            isJudge[i].append(j)
            trustCnt[j]+=1
        for k,v in isJudge.items():
            if len(v)==0 and trustCnt[k]==n-1:
                return k
        
        return -1