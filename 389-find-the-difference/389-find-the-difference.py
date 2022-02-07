class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countDict = defaultdict(int)
        for i in s:
            countDict[i]+=1
        for i in t:
            countDict[i]-=1
        for key,value in countDict.items():
            if value!=0:
                return key