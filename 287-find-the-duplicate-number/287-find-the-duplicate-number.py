class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for bit in range(32):
            mask = 1<<bit
            totCount = currCount = 0
            for i in range(0, n):
                if i&mask:
                    totCount+=1
                if nums[i]&mask:
                    currCount+=1
            if currCount > totCount:
                print(mask)
                ans|=mask
        return ans