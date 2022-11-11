class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0
        i = 0
        n = len(nums)
        while i<n:
            j = i+1
            while j<n and nums[j]==nums[j-1]:
                j+=1
            nums[curr_idx]=nums[i]
            curr_idx+=1
            i=j
        return curr_idx
            