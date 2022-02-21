class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = math.inf
        majorityElementCount = 0
        for i in nums:
            if majorityElementCount == 0:
                majorityElement = i
                majorityElementCount = 1
            elif i != majorityElement:
                majorityElementCount -= 1
            else:
                majorityElementCount += 1
        return majorityElement