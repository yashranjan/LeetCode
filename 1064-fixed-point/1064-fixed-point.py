class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            val = arr[mid]
            if val == mid:
                ans = mid
                r = mid-1
            elif val > mid:
                r = mid-1
            else:
                l = mid+1
        
        return ans