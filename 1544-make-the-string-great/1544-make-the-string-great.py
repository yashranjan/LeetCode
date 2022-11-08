class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)<=1:
            return s
        idx = 0
        n = len(s)
        while idx<n:
            n = len(s)
            if idx+1<n and s[idx]!=s[idx+1] and (s[idx]==s[idx+1].lower() or s[idx].lower()==s[idx+1]):
                s = s[:idx]+s[idx+2:]
                idx=max(0, idx-1)
            else:
                idx+=1
        return s