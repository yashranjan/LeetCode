class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, candidateCnt = None, 0
        for i in nums:
            if candidateCnt == 0:
                candidate = i
            candidateCnt += (1 if i==candidate else -1)
        return candidate
        