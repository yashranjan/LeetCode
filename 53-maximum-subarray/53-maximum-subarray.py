class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(nums, left, right):
            if left > right:
                return -math.inf
            
            mid = (left+right)//2

            curr = 0
            bestLeftSum = bestRightSum = 0

            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                bestLeftSum = max(bestLeftSum, curr)
            
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                bestRightSum = max(bestRightSum, curr)
            
            bestCurrSum = bestLeftSum + bestRightSum + nums[mid]
            
            bestLeftSum = solve(nums, left, mid-1)
            bestRightSum = solve(nums, mid+1, right)
            
            return max(bestCurrSum, bestLeftSum, bestRightSum)
        
        return solve(nums, 0, len(nums)-1)
        
        