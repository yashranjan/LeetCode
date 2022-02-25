class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ans = 0
        firstLst = version1.split('.')
        secondLst = version2.split('.')
        
        i = j = 0
        n, m = len(firstLst), len(secondLst)
        
        while i<n or j<m:
            first = firstLst[i] if i<n else '0'
            second = secondLst[j] if j<m else '0'
            first = int(first)
            second = int(second)
            if first > second:
                ans = 1
                break
            elif second > first:
                ans = -1
                break
            i += 1
            j += 1

        return ans