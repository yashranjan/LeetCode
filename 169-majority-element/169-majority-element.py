class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, majorFreq = None, 0
        for i in nums:
            if major is None:
                major = i
                majorFreq += 1
            elif i == major:
                majorFreq += 1
            else:
                majorFreq -= 1
            if majorFreq == 0:
                major, majorFreq = None, 0
        
        return major