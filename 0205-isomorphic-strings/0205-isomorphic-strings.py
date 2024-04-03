class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst = list(t)
        
        curr_cnt = 0
        char_map_1 = dict()
        char_map_2 = dict()
        
        for first_c, second_c in zip(s_lst, t_lst):
            char_cnt_1 = char_cnt_2 = 0
            if first_c not in char_map_1 and second_c not in char_map_2:
                char_map_1[first_c] = curr_cnt
                char_map_2[second_c] = curr_cnt
                curr_cnt += 1
            elif (first_c not in char_map_1 and second_c in char_map_2) or (first_c in char_map_1 and second_c not in char_map_2):
                return False
            char_cnt_1 = char_map_1[first_c]
            char_cnt_2 = char_map_2[second_c]
            if char_cnt_1 != char_cnt_2:
                return False        
        return True