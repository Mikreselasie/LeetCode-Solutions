class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left, right, count = 0, 1, 0

        while right < len(colors) + k-1:
            if colors[right%(len(colors))] + colors[(right-1)%(len(colors))] != 1:
                left = right
            right += 1
            if right - left == k:
                count += 1
                left += 1
        return count