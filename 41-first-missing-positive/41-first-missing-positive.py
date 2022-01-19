class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            while curr-1>=0 and curr-1<n and nums[curr-1]!=curr:
                tmp = nums[curr-1]
                nums[curr-1]=curr
                curr = tmp
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
