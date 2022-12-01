class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s)-1
        l_cnt = r_cnt = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        while l<r:
            l_c, r_c = s[l], s[r]
            if l_c.lower() in vowels:
                l_cnt += 1
            if r_c.lower() in vowels:
                r_cnt += 1
            l, r = l+1, r-1
        
        return l_cnt == r_cnt