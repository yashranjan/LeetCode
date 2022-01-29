class Solution:
    def mergeArray(self, nums, st, mid, et):
        curr = 0
        tmp = []
        i, j = st, mid+1
        p = mid+1
        lastI = st-1
        while i<=mid:
            while p<=et and nums[i]>2*nums[p]:
                p+=1
            curr += p-(mid+1)
            while j<=et and nums[j]<=nums[i]:
                tmp.append(nums[j])
                j+=1
            tmp.append(nums[i])
            i+=1
        while j<=et:
            tmp.append(nums[j])
            j+=1

        nums[st:et+1] = tmp
        return curr
    
    def countInversions(self, nums, st, et):
        if st>=et:
            return 0
        mid = (st+et)//2
        ans = self.countInversions(nums, st, mid) + self.countInversions(nums, mid+1, et)
        ans += self.mergeArray(nums, st, mid, et)
        return ans

    def reversePairs(self, nums: List[int]) -> int:
        ans = self.countInversions(nums, 0, len(nums)-1)
        return ans