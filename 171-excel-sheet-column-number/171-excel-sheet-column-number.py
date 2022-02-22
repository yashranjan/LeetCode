class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        currWeight = 1
        ans = 0
        for i in range(len(columnTitle)-1, -1, -1):
            currVal = ord(columnTitle[i])-ord('A')+1
            ans += (currWeight*currVal)
            currWeight *= 26
        
        return ans
        