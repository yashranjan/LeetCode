class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hashSet = set()
        for i in nums:
            hashSet.add(i)
        for i in range(n+1):
            if i in hashSet:
                continue
            return i
        return -1