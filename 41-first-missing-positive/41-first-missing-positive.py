class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        elementsSeen = set([i for i in nums if i>0])
        if not len(elementsSeen):
            return 1
        maxSeen = max(elementsSeen)
        for i in range(1,maxSeen):
            if i not in elementsSeen:
                return i
        else:
            return maxSeen+1
        