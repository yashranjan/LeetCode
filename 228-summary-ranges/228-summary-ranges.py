class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        curr = -math.inf
        n = len(nums)
        i = 0
        while i<n:
            if curr == -math.inf:
                curr = i
            j = i+1
            while j<n and nums[j]==nums[j-1]+1:
                j += 1
            if j == i+1:
                ans.append('{}'.format(nums[i]))
            else:
                ans.append('{}->{}'.format(nums[i], nums[j-1]))
            
            curr = -math.inf
            i = j
        
        return ans
                