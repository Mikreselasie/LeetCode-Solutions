class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        my_sum = 0
        left = 0
        right = len(piles) - 2
        while left < right:
            my_sum += sorted_piles[right]
            right -= 2
            left += 1
        return my_sum
        