class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        rem = 0
        while n >= 4:
            rem = n%4
            n = n/4
        return n == 1 and rem==0
        