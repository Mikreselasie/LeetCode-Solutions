class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_no = nums[0]
        current = nums[0]

        for i in range(1,len(nums)):
            current = max(nums[i],current + nums[i])
            max_no = max(max_no,current)
        return max_no
        