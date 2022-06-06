class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-2):
            sumToFind = -nums[i]
            l, r = i+1, n-1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l != r:
                currSum = nums[l] + nums[r]
                if currSum == sumToFind:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif currSum > sumToFind:
                    r -= 1
                else:
                    l += 1
        
        return ans