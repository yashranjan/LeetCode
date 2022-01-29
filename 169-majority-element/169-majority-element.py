class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, candidateCnt = math.inf, 0
        for i in nums:
            if candidate == math.inf:
                candidate = i
            if i == candidate:
                candidateCnt += 1
            else:
                candidateCnt -= 1
            if candidateCnt == 0:
                candidate = math.inf
        return candidate
        