class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        diffCnt = defaultdict(int)
        for i in tasks:
            diffCnt[i]+=1
        
        ans = 0
        for k, v in diffCnt.items():
            if v==1:
                return -1
            curr = 0
            if v%3==0:
                curr += (v//3)
            else:
                curr += v//3+1
            ans += curr
        
        return ans