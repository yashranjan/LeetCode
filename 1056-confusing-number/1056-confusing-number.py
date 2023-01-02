class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotMap = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6] 
        
        curr = n
        res = 0
        while curr>=1:
            dig = curr%10
            curr //= 10
            val = rotMap[dig]
            if val == -1:
                return False
            res = res*10+val
        
        return n!=res