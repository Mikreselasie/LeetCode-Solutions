class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ptr = 0
        # write your code here
        while ptr < len(nums):
            if nums[ptr]-1 == ptr or nums[nums[ptr]-1] == nums[ptr] : ptr += 1
            else: nums[nums[ptr]-1],nums[ptr] = nums[ptr],nums[nums[ptr]-1]

        return [i+1 for i in range(len(nums)) if nums[i] != i+1]
