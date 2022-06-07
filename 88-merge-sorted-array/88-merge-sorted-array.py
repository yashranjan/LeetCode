class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        currIdx = m+n-1
        firstEnd = m-1
        secondEnd = n-1
        
        while firstEnd>=0 and secondEnd>=0:
            val1, val2 = nums1[firstEnd], nums2[secondEnd]
            if val1 <= val2:
                nums1[currIdx] = val2
                currIdx, secondEnd = currIdx-1, secondEnd-1
            else:
                nums1[currIdx] = val1
                currIdx, firstEnd = currIdx-1, firstEnd-1
        
        while firstEnd>=0:
            nums1[currIdx] = nums1[firstEnd]
            currIdx, firstEnd = currIdx-1, firstEnd-1
        
        while secondEnd>=0:
            nums1[currIdx] = nums2[secondEnd]
            currIdx, secondEnd = currIdx-1, secondEnd-1
        
        