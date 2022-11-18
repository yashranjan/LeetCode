class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_ans = -1
        hash_set = set()
        for i in nums:
            for j in hash_set:
                if i+j<k:
                    max_ans = max(max_ans, i+j)
            hash_set.add(i)
        return max_ans