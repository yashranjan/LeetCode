class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, l, r = 0, 0, len(nums)-1
        
        while curr<=r:
            if nums[curr]==1: 
                curr+=1
            elif nums[curr]==0:
                nums[curr], nums[l] = nums[l], nums[curr]
                curr, l = curr+1, l+1
            elif nums[curr]==2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r-=1
        