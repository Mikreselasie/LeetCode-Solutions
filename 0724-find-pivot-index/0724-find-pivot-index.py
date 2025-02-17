class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x = 0
        y = sum(nums)

        for j in range(len(nums)):
            if x == y - nums[j] - x:
                return j
            x += nums[j]
        return -1


        