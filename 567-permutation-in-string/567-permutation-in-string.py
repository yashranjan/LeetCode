class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        firstHashMap = defaultdict(int)
        for s in s1:
            firstHashMap[s] += 1
        currHashMap = defaultdict(int)
        n = len(s1)
        for j in range(len(s2)):
            currHashMap[s2[j]] += 1
            if j >= n:
                currHashMap[s2[j-n]] -= 1
                if currHashMap[s2[j-n]] == 0:
                    del currHashMap[s2[j-n]]
            if currHashMap == firstHashMap:
                return True

        return False