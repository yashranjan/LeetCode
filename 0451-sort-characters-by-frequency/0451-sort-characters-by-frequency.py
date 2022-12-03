from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ans = []
        for c, f in counter.most_common():
            ans.append(c*f)
        return ''.join(ans)