class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            current_area = (min(height[left],height[right]))* (right-left)
            max_area = max(max_area,current_area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         min_height = min(height[i],height[j])
        #         area = (j-i) * min_height
        #         max_area = max(area,max_area)
        return max_area

        