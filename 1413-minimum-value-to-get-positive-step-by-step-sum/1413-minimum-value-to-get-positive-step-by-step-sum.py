class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        totSum = 0
        smallestSum = 0
        for i in nums:
            totSum += i
            smallestSum = min(smallestSum, totSum)
        return abs(smallestSum)+1 if smallestSum < 0 else 1