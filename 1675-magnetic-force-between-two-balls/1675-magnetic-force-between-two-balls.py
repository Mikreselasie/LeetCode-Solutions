class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def is_valid(num):
            basket = 1
            prev = position[0]

            for val in position[1:]:
                if val - prev>= num:
                    prev = val
                    basket += 1
            return basket >= m
        left = 0
        right = max(position)-min(position)

        while left <= right:
            mid = (left+right)//2

            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right