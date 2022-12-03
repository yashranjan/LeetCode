from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())
        
        buckets = [[] for i in range(max_freq+1)]
        
        for c, i in counter.items():
            buckets[i].append(c)

        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                ans.append(c*i)

        return ''.join(ans)