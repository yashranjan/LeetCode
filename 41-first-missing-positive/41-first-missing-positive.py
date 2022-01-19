class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, end = 0, len(nums)
        while i!=end:
            val = nums[i]
            if val==i+1:
                i+=1
            elif val<=0 or val>end or val==nums[val-1]:
                end-=1
                nums[i], nums[end] = nums[end], nums[i]
            else:
                nums[i], nums[val-1] = nums[val-1], nums[i]
        return i+1
