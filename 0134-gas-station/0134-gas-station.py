class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        totTank, currTank = 0, 0
        stStation = 0
        for i in range(n):
            totTank += gas[i]-cost[i]
            currTank += gas[i]-cost[i]
            if currTank<0:
                stStation = i+1
                currTank = 0
        
        return stStation if totTank>=0 else -1