class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = m-1, n-1
        curr = m+n-1
        while first>=0 or second>=0:
            if first>=0 and second>=0:
                if nums1[first] >= nums2[second]:
                    nums1[curr] = nums1[first]
                    curr, first = curr-1, first-1
                else:
                    nums1[curr] = nums2[second]
                    curr, second = curr-1, second-1
            elif first>=0:
                nums1[curr] = nums1[first]
                curr, first = curr-1, first-1
            else:
                nums1[curr] = nums2[second]
                curr, second = curr-1, second-1
        
        