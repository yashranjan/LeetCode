class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst = list(t)
        
        curr_cnt = 0
        char_map = dict() # type: (str, int)
        
        for idx, c in enumerate(s_lst):
            char_cnt = 0
            if c not in char_map:
                char_map[c] = curr_cnt
                curr_cnt += 1
            char_cnt = char_map[c]
            s_lst[idx] = char_cnt
        
        char_map.clear()
        curr_cnt = 0
        
        for idx, c in enumerate(t_lst):
            char_cnt = 0
            if c not in char_map:
                char_map[c] = curr_cnt
                curr_cnt += 1
            char_cnt = char_map[c]
            t_lst[idx] = char_cnt
        
        for (i, j) in zip(s_lst, t_lst):
            if i!=j:
                return False
        
        return True
                
                
        