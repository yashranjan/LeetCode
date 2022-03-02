class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        s_n = len(s)
        t_n = len(t)
        while s_i < s_n and t_i < t_n:
            if s[s_i] == t[t_i]:
                s_i, t_i = s_i+1, t_i+1
            else:
                t_i += 1
        
        return s_i == s_n