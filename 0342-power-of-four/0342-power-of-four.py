class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def to_base(x):
            if x == 1:
                return True
            if x % 4 != 0 or x == 0:
                return False
            return to_base(x//4)
        return to_base(n)            