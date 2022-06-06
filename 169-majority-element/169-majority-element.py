class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for i in nums:
            hashMap[i] += 1
        major = len(nums)//2
        for key, value in hashMap.items():
            if value > major:
                return key
        return -1