class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        lstLen = len(flowerbed)
        for i in range(lstLen):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==lstLen-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                cnt += 1
            if cnt>=n: break
        return cnt>=n
        