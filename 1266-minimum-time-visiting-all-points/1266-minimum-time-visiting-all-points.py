class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1,len(points)):
            hor_gap = abs(points[i][0] - points[i-1][0])
            ver_gap = abs(points[i][1] - points[i-1][1])
            ans += max(hor_gap,ver_gap)
        return ans
        