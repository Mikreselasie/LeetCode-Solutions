class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        right = 1
        left = 0
        count = 0
        while right < len(colors):
            no = colors[right-1]
            if no == colors[right]:
                left = right
            right += 1
            if right - left == k:
                count += 1
                left += 1
        return count
            

