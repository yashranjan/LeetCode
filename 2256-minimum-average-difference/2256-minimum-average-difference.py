class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        curr_sum = 0
        n = len(nums)
        
        ans = 10**10
        ans_idx = -1
        for i in range(n):
            curr_sum += nums[i]
            left_val = (curr_sum//(i+1))
            right_val = ((tot_sum-curr_sum)//(n-i-1)) if i+1<n else 0
            curr_val = abs(left_val-right_val)
            if curr_val<ans:
                ans = curr_val
                ans_idx = i
            
        return ans_idx