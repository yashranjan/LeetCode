class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = count = 0
        hashMap = {0:-1}
        for i in range(len(nums)):
            count += (1 if nums[i] else -1)
            if count in hashMap:
                maxLen = max(maxLen, i-hashMap[count])
            else:
                hashMap[count] = i
        return maxLen