class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currAns = []
        n = len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, n-1
            target = -nums[i]
            while j<k:
                currSum = nums[j] + nums[k]
                if currSum == target:
                    currAns.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                elif currSum > target:
                    k -= 1
                else:
                    j += 1
        return currAns
                    