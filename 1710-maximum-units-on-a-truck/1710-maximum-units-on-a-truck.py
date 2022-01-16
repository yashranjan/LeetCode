class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxesPerUnitSize = [0]*1001
        for i in boxTypes:
            boxesPerUnitSize[i[1]] += i[0]
        ans = 0
        for i in range(1000, -1, -1):
            boxesOfCurrentType = min(boxesPerUnitSize[i], truckSize)
            ans += (boxesOfCurrentType*i)
            truckSize -= boxesOfCurrentType
        
        return ans
        