from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ans = True
        cnt_dict_a = [0]*26
        cnt_dict_b = [0]*26
        word_bit_a = word_bit_b = 0 
        for i in word1:
            cd = ord(i)-ord('a')
            cnt_dict_a[cd] += 1
            if cnt_dict_a[cd] == 1:
                word_bit_a ^= (1<<cd)

        for i in word2:
            cd = ord(i)-ord('a')
            cnt_dict_b[cd] += 1
            if cnt_dict_b[cd] == 1:
                word_bit_b ^= (1<<cd)            
        
        values_a = sorted(cnt_dict_a)
        values_b = sorted(cnt_dict_b)

        return word_bit_a == word_bit_b and values_a == values_b