class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = n-1
        while r-1>=0 and nums[r]<=nums[r-1]:
            r -= 1
        if r-1<0:
            nums.sort()
            return
        idx = r-1
        r = n-1
        val = nums[idx]
        smallestGreaterIdx = None
        while r>idx:
            if nums[r]>val:
                if not smallestGreaterIdx: 
                    smallestGreaterIdx = r
                elif nums[r]-val<nums[smallestGreaterIdx]-val: 
                    smallestGreaterIdx = r
            r -= 1
        nums[idx], nums[smallestGreaterIdx] = nums[smallestGreaterIdx], nums[idx]
        nums[idx+1:] = nums[n-1:idx:-1]