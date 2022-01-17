class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        valuesSeenSoFar = {}
        dups = set()
        for i in range(n):
            if i in dups:
                continue
            dups.add(i)
            for j in range(i+1,n):
                target = -(nums[i]+nums[j])
                if target in valuesSeenSoFar and valuesSeenSoFar[target] == i:
                    res.add(tuple(sorted((nums[i], nums[j], target))))
                valuesSeenSoFar[nums[j]] = i
        return res