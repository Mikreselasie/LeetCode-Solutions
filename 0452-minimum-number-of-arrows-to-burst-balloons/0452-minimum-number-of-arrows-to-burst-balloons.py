class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        intersection = points[0]
        ans = 1
        for point in points:
            intersection = [max(point[0],intersection[0]),min(point[1],intersection[1])]

            if intersection[0] > intersection[1]:
                intersection = point
                ans += 1
        return ans