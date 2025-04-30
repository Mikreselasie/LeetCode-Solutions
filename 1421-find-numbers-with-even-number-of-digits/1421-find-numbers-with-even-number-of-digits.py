class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0

        for num in nums:
            digits = 0
            while num:
                digits += 1
                num //=10
            if digits%2 == 0: cnt += 1
        
        return cnt

        