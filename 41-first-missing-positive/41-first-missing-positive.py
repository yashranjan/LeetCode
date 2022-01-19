class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1
        for i in range(n):
            val = abs(nums[i])
            if nums[val-1]>0:
                nums[val-1]=-nums[val-1]
        for i in range(n):
            if nums[i]>0:
                return i+1
        else:
            return n+1