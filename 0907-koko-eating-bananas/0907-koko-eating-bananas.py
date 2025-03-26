class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 1

        def good(rate):
            hrs = 0
            for bananas in piles:
                hrs += ceil(bananas/rate)
                if hrs > h:
                    return False
            return True


        while left <= right:
            mid = (left + right)//2

            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
