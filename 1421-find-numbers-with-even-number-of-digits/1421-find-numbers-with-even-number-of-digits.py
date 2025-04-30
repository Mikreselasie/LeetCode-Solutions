class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0

        for num in nums:
            digits = 0
            while num: 
                digits += 1
                num //= 10
            if not digits%2: cnt += 1
        return cnt