class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        new_ptr = 0
        for i in range(n):
            if nums[i] != 0:
                nums[new_ptr], nums[i] = nums[i], nums[new_ptr]
                new_ptr += 1
        
        return nums