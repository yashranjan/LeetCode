class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = [i for i in s.split() if i]
        s_lst.reverse()
        n = len(s_lst)
        l = r = 0
        while l<n:
            while r<n and s_lst[r]!=' ':
                r+=1
            s_lst[l:r].reverse()
            l = r+1
            r+=1
        return ' '.join(s_lst)
                