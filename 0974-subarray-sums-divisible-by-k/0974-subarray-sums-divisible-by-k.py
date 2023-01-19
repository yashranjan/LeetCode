class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        modGroup = [0]*k
        modGroup[0] = 1
        prefixMod = 0
        
        for i in nums:
            prefixMod = (prefixMod + i % k + k) % k
            ans += modGroup[prefixMod]
            modGroup[prefixMod] += 1
        
        return ans