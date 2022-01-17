class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        wordDict = {}
        matches = True
        if len(pattern) != len(s): return False
        wordsInserted = set()
        for p, w in zip(pattern, s):
            if p in wordDict and wordDict[p] != w:
                return False
            elif p not in wordDict:
                if w in wordsInserted:
                    return False
                wordDict[p] = w
                wordsInserted.add(w)
        return True