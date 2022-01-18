class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if (n==1 and flowerbed[0]==0) or (n==0):
                return True
            elif n>1 or (n==1 and flowerbed[0]==1):
                return False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n:
                if i-1>=0 and flowerbed[i-1]==0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
                    n -= 1
                    flowerbed[i] = 1
                elif i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
                    n -= 1
                    flowerbed[i] = 1
                elif i==len(flowerbed)-1 and i-1>=0 and flowerbed[i-1]==0:
                    n -= 1
                    flowerbed[i] = 1
            if n==0:
                break
        return n==0
        