class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, -math.inf
        st, et = 0, 0
        for idx, i in enumerate(nums):
            if currSum == 0:
                st = idx
            currSum += i
            if currSum > maxSum:
                maxSum = currSum
                et = idx
            if currSum < 0:
                currSum = 0
        print(st, et)
        return maxSum
        
        