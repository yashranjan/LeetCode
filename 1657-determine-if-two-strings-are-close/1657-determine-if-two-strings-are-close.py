from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ans = True
        cnt_dict_a = [0]*26
        cnt_dict_b = [0]*26
        
        for i in word1:
            cnt_dict_a[ord(i)-ord('a')] += 1
        for i in word2:
            cnt_dict_b[ord(i)-ord('a')] += 1
        
        keys_a = set(word1)
        keys_b = set(word2)
        
        values_a = sorted(cnt_dict_a)
        values_b = sorted(cnt_dict_b)
        
        return keys_a == keys_b and values_a == values_b