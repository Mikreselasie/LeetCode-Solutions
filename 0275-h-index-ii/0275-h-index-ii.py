class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        while left <= right:
            mid = (left+right)//2
            if len(citations)-bisect_left(citations, mid) >= mid: left = mid + 1
            else: right = mid - 1
        return right
