class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        min_no = 0
        max_no = int(c**0.5)

        while min_no <= max_no:
            if min_no**2 + max_no**2 > c:
                max_no -= 1
            elif min_no**2 + max_no**2 < c:
                min_no += 1
            else:
                return True
        return False



        