class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(val, idx) for idx,val in enumerate(nums)]
        nums.sort()
        l, r = 0, len(nums)-1
        while l<r:
            curr = nums[l][0] + nums[r][0]
            if curr == target:
                return (nums[l][1], nums[r][1])
            elif curr>target:
                r -= 1
            else:
                l += 1
        return (-1, -1)
        