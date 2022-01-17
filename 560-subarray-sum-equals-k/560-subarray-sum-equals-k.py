class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        sumDict = {}
        curr = 0
        for i in nums:
            curr += i
            if curr == k: ans += 1
            if (curr-k) in sumDict: ans += sumDict[curr-k]
            if curr in sumDict:
                sumDict[curr] += 1
            else:
                sumDict[curr] = 1
        return ans
                