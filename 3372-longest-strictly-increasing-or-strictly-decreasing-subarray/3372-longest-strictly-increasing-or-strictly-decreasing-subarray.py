class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 1
        i = 1
        while i < len(nums):
            temporary_count = 1
            while i < len(nums) and nums[i] > nums[i-1]:
                temporary_count += 1
                i += 1

            count = max(count,temporary_count)
            temporary_count = 1 
            while i < len(nums) and nums[i] < nums[i-1]:
                temporary_count += 1
                i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
            count = max(count,temporary_count)

        return count

            




        