class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-2):
            sumToFind = -nums[i]
            l, r = i+1, n-1
            while l != r:
                currSum = nums[l] + nums[r]
                if currSum == sumToFind:
                    tmpAns = '{} {} {}'.format(nums[i], nums[l], nums[r])
                    if tmpAns not in ans:
                        ans.add(tmpAns)
                    l += 1
                elif currSum > sumToFind:
                    r -= 1
                else:
                    l += 1
        
        return [i.split(' ') for i in ans]