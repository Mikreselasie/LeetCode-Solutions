class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        temp_sum = sum(nums[left:right+1])
        max_average = temp_sum / k
        while right < len(nums)-1:
            temp_sum = temp_sum + nums[right+1] - nums[left]
            right += 1
            left += 1
            temp_average = temp_sum / k
            max_average = max(max_average,temp_average)
        return max_average
        