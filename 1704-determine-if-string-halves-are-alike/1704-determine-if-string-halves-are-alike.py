class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        mid = len(s)/2
        cnt = 0
        for i in range(len(s)):
            if s[i] in vowels:
                cnt += (1 if i<mid else -1)
        return cnt == 0
        
        # return len([i for i in s[0:len(s)//2] if i in vowels]) == len([i for i in s[len(s)//2:] if i in vowels])