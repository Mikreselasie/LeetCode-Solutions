class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)
        
        def check(limit_y):
            area = 0
            for x,y,l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y,l)

            return total_area <= area * 2
        
        high = max_y
        low = 0
        eps = 1e-5

        while abs(high - low) > eps:
            mid = (high+low)/2
            if check(mid):
                high = mid
            else:
                low = mid

        return high

        
        