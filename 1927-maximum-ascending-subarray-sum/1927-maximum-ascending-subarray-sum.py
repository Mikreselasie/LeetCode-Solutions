class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        index = 1
        max_no = 0
        if len(nums) == 1:
            return nums[0]
        while index < len(nums):
            temporary = 0
            while index <= len(nums)-1 and nums[index] > nums[index - 1]:
                temporary += nums[index - 1]
                index += 1
            else:
                temporary += nums[index - 1]
                index += 1
            max_no = max(max_no, temporary)
        return max_no
            

        