class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = defaultdict(int)
        for i in arr:
            cnt_dict[i] += 1
        
        return len(cnt_dict.keys()) == len(set(cnt_dict.values()))