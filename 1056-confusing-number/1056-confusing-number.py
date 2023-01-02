class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotMap = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6] 
        
        n = str(n)
        ans = []
        for i in n:
            idx = ord(i)-ord('0')
            val = rotMap[idx]
            if val == -1:
                return False
            ans.append(chr(ord('0')+val))
        return n != ''.join(ans[::-1])