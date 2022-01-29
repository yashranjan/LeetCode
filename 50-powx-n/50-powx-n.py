class Solution:
    def multiply(self, x, n):
        if n==1:
            return x
        ans = self.multiply(x, n//2)
        ans *= ans
        if n%2==1:
            ans *= x
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
        