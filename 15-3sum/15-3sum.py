class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        for i in range(n):
            valuesSeenSoFar = set()
            for j in range(i+1,n):
                target = -(nums[i]+nums[j])
                if target in valuesSeenSoFar:
                    res.add(tuple(sorted((nums[i], nums[j], target))))
                valuesSeenSoFar.add(nums[j])
        return res