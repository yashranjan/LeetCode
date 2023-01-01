class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        if len(pattern) != len(s): return False
        wrdPat = {}
        incl = set()
        
        for i,j in zip(pattern, s):
            # print(i, j)
            if i not in wrdPat:
                wrdPat[i] = j
                if j in incl:
                    return False
                incl.add(j)
            elif wrdPat[i] != j:
                return False
        
        return True