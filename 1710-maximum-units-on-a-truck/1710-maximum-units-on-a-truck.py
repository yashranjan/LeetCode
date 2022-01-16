class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = curr = 0
        while truckSize>0 and curr<len(boxTypes):
            minBoxOfThisType = min(boxTypes[curr][0], truckSize)
            ans += (boxTypes[curr][1]*minBoxOfThisType)
            truckSize -= minBoxOfThisType
            curr += 1
        return ans