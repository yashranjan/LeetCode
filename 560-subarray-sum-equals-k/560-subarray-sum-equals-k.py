class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        currSum = ans = 0
        for i in nums:
            currSum += i
            if currSum-k in hashMap:
                ans += hashMap[currSum-k]
            hashMap[currSum] = hashMap.get(currSum, 0)+1
        return ans