from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        cnt_dict_a = [0]*26
        cnt_dict_b = [0]*26
        word_bit_a = word_bit_b = 0 
        
        for i in word1:
            cd = ord(i)-ord('a')
            cnt_dict_a[cd] += 1

        for i in word2:
            cd = ord(i)-ord('a')
            cnt_dict_b[cd] += 1
        
        val_bit = 0

        for i,j in zip(cnt_dict_a, cnt_dict_b):
            if i>0 and j==0 or i==0 and j>0:
                return False
        cnt_dict_a.sort()
        cnt_dict_b.sort()

        return cnt_dict_a == cnt_dict_b