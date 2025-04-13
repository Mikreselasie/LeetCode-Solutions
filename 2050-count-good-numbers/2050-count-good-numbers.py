class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = ceil(n/2)
        odds = n - evens
        total = (pow(5,evens,10**9 +7) *pow(4,odds,10**9 +7))%(10**9 +7)
        return total     