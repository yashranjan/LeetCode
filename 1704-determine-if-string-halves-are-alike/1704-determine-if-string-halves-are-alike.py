class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        
        return len([i for i in s[0:len(s)//2] if i in vowels]) == len([i for i in s[len(s)//2:] if i in vowels])