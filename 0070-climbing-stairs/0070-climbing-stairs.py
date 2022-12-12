class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1+sqrt5)/2
        psi = (1-sqrt5)/2
        return int((math.pow(phi, n+1)-math.pow(psi, n+1))//sqrt5)
        