# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

from random import randint
class Solution:
    def guessNumber(self, n: int) -> int:
        a, b = 1, n+1
        while True:
            num = (a+b)//2
            ans = guess(num)
            if ans==0:
                return num
            elif ans>0:
                a=num+1
            else:
                b=num-1
                
        