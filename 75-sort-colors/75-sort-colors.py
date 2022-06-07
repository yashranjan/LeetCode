class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)        
        l, r = 0, n-1
        curr = 0
        while curr <= r:
            val = nums[curr]
            if val == 0:
                nums[curr], nums[l] = nums[l], val 
                l += 1
                curr += 1
            elif val == 1:
                curr += 1
            else:
                nums[curr], nums[r] = nums[r], val
                r -= 1
        
        
        