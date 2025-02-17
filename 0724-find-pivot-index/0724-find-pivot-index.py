class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for j in range(len(nums)):
            if j > 0:
                if nums[j-1] == nums[-1] - nums[j]:
                    return j
            else:
                if nums[-1] -nums[j] == 0:
                    return j
        return -1


        