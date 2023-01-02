class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cntCapitals = len([i for i in word if 'A'<=i<='Z'])
        
        return cntCapitals==len(word) or not cntCapitals or ('A'<=word[0]<='Z' and cntCapitals==1)