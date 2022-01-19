class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for i in nums:
            if i in numSet:
                return i
            numSet.add(i)
        return -1