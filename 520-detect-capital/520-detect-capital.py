class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capsCnt = len([i for i in word if 'A'<=i<='Z'])
        if capsCnt==len(word) or capsCnt==0 or capsCnt==1 and 'A'<=word[0]<='Z':
            return True
        return False
        