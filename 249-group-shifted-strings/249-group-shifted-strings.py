class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = []
        n = len(strings)
        marked = [False]*n
        for i in range(n):
            if marked[i]: continue
                
            orig = strings[i]
            marked[i] = True
            currAns = [orig]
            for j in range(i+1, n):
                curr = strings[j]
                if not marked[j] and len(orig) == len(curr):
                    diff = math.inf
                    isSame = True
                    for f,s in zip(orig, curr):
                        if diff == math.inf:
                            diff = (ord(s)-ord(f)+26)%26
                        else:
                            if (ord(s)-ord(f)+26)%26 != diff:
                                isSame = False
                                break
                    if isSame:
                        marked[j] = True
                        currAns.append(curr)
            ans.append(currAns)
        return ans