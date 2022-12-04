class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = []
        suffix_sum = []
        curr_sum = 0
        n = len(nums)
        for i in range(n):
            if i==0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            prefix_sum.append(curr_sum)
        
        curr_sum = 0
        print(nums)
        for i in range(n-1, -1, -1):
            if i==n-1:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            suffix_sum.append(curr_sum)
        
        suffix_sum.reverse()
        
        ans = 10**10
        ans_idx = -1
        for i in range(n):
            left_val = (prefix_sum[i]//(i+1))
            right_val = (suffix_sum[i+1]//(n-i-1)) if i+1<n else 0
            curr_val = abs(left_val-right_val)
            if curr_val<ans:
                ans = curr_val
                ans_idx = i
            
        return ans_idx