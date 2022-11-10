class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<=1:
            return s
        curr_idx = 0
        lst_idx = len(s)-1
        while curr_idx<lst_idx:
            if curr_idx>=0 and curr_idx+1<=lst_idx and s[curr_idx]==s[curr_idx+1]:
                s = s[:curr_idx]+s[curr_idx+2:]
                curr_idx-=1
            else:
                curr_idx+=1
            lst_idx = len(s)-1
        
        return s
        