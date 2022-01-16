class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = m-1, n-1
        curr = m+n-1
        for p in range(n+m-1, -1, -1):
            if second<0:
                break
            if first>=0 and nums1[first]>=nums2[second]:
                nums1[p] = nums1[first]
                first -= 1
            else:
                nums1[p] = nums2[second]
                second -= 1