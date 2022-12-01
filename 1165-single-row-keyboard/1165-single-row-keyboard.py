class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        tot = 0
        idx_map = [0]*26
        for idx, i in enumerate(keyboard):
            idx_map[ord(i)-ord('a')]= idx

        last_idx = 0
        for i in word:
            idx = idx_map[ord(i)-ord('a')]
            tot += abs(idx-last_idx)
            last_idx = idx
        return tot