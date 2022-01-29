class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            cnt = len([1 for j in nums if j&(1<<i)>0])
            if cnt > (n-cnt):
                if i==31:
                    ans = -((1<<31)-ans)
                else:
                    ans |= (1<<i)
        return ans