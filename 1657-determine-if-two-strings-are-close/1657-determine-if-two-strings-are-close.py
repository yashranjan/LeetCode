from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ans = True
        cnt_dict_a = defaultdict(int)
        cnt_dict_b = defaultdict(int)
        
        for i in word1:
            cnt_dict_a[i] += 1
        for i in word2:
            cnt_dict_b[i] += 1
        
        keys_a = set(word1)
        keys_b = set(word2)
        
        values_a = sorted(cnt_dict_a.values())
        values_b = sorted(cnt_dict_b.values())
        
        return keys_a == keys_b and values_a == values_b