class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cntCapitals = 0
        for i in word:
            if 'A'<=i<='Z':
                cntCapitals += 1
        
        if cntCapitals==len(word) or not cntCapitals:
            return True
        if 'A'<=word[0]<='Z' and cntCapitals==1:
            return True
        return False