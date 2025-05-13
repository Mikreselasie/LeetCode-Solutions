class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        arr = 0
        for i in range(len(nums)):
            total ^= (i+1)
            arr ^= nums[i]
        return total ^ arr
