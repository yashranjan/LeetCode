class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_ans = -1
        nums.sort()
        left, right = 0, len(nums)-1
        while left<right:
            curr_sum = nums[left]+nums[right]
            if curr_sum<k:
                max_ans = max(max_ans, curr_sum)
                left += 1
            else:
                right -= 1
        return max_ans