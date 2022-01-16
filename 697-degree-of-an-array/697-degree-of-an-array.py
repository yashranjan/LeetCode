class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequencyWithIndices = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in frequencyWithIndices:
                frequencyWithIndices[val][0] += 1
                frequencyWithIndices[val][2] = i
            else:
                frequencyWithIndices[val] = [1, i, i]
        maxFreq, minLen = 0, 0
        for i in frequencyWithIndices:
            currFreq, st, et = frequencyWithIndices[i]
            if currFreq > maxFreq:
                maxFreq = currFreq
                minLen = et-st+1
            elif currFreq == maxFreq:
                minLen = min(minLen, et-st+1)
        return minLen