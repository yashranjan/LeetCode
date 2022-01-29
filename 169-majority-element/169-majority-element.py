class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = defaultdict(int)
        for i in nums:
            countDict[i]+=1
        n = len(nums)
        for key, value in countDict.items():
            if value>n//2:
                return key
        return -1
        