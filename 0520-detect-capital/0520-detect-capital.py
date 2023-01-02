class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cntCapitals = 0
        for i in word:
            if 'A'<=i<='Z':
                cntCapitals += 1
        
        return cntCapitals==len(word) or not cntCapitals or ('A'<=word[0]<='Z' and cntCapitals==1)