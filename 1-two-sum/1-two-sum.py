class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = nums[i]
            isFound = False
            for j in range(len(nums)):
                if nums[j] == (target-curr) and j!=i:
                    return [i,j]
        return []