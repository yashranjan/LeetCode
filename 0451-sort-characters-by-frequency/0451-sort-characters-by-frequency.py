from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        items = list(counter.items())
        items.sort(key=lambda x:x[1], reverse=True)
        return ''.join([i*j for i,j in items])
        return ''.join(sorted(s, key=lambda x:counter[x])[::-1])