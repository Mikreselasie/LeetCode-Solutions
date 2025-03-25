# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1

        while left <= n:
            middle = (left + n)//2
            if isBadVersion(middle):
                n = middle - 1
            else:
                left = middle + 1
        return left
            
