class Solution:
    def mySqrt(self, x: int) -> int:
        high,low = x,0
        sqrt = 0

        while low <= high:
            mid = (low + high)//2
            if mid*mid <= x:
                sqrt = mid
                low = mid + 1
            else:
                high = mid - 1
        return sqrt