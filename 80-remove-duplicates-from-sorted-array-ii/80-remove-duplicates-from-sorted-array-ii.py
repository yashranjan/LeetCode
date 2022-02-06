class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        currIdx = 0
        i = 0
        while i<n:
            curr = nums[i]
            j = i+1
            nums[currIdx] = curr
            currIdx += 1
            isFirst = False
            while j<n and curr == nums[j]:
                if not isFirst:
                    nums[currIdx] = nums[j]
                    isFirst = True
                    currIdx += 1
                j += 1
            i = j
        return currIdx