class Solution:
    def solve(self, nums, idx):
        if idx>=len(nums):
            return 0

        if idx in self.cache:
            return self.cache[idx]
        
        ans = max(self.solve(nums, idx+1), self.solve(nums, idx+2)+nums[idx])
        self.cache[idx] = ans
        
        return ans
    
    def rob(self, nums: List[int]) -> int:
        self.cache = dict()
        return self.solve(nums, 0)