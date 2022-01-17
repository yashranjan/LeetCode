class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currAns = set()
        n = len(nums)
        for i in range(n):
            j, k = i+1, n-1
            target = -nums[i]
            while j<k:
                currSum = nums[j] + nums[k]
                if currSum == target:
                    currAns.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif currSum > target:
                    k -= 1
                else:
                    j += 1
        return [list(i) for i in currAns]
                    