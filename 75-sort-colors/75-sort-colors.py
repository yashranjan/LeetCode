class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countAll = [0]*3
        for i in nums:
            countAll[i] += 1
        
        currInd = 0
        for idx, val in enumerate(countAll):
            freq = val
            while freq:
                nums[currInd] = idx
                currInd += 1
                freq -= 1
        
        