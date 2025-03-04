class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:
            if target % 2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                target //= 2
            elif maxDoubles == 0:
                return target + count - 1
            else:
                target -= 1
            count += 1
        return count