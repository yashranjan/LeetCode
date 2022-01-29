class Solution:
    def multiply(self, x, n):
        ans = 1
        curr = x
        while n:
            if (n%2) == 1:
                ans = ans*curr
            curr *= curr
            n //= 2
        return ans
    
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        toBeNegated = -1 if x<0 and n%2==1 else 1
        toBeDivided = 1 if n<0 else 0
        x, n = abs(x), abs(n)
        ans = self.multiply(x, n)
        if toBeDivided:
            ans = 1/ans
        ans *= toBeNegated
        return ans
        