class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        holder = 0

        while seeker < len(nums) and holder < len(nums):
            if nums[seeker] != 0:
                nums[seeker],nums[holder] = nums[holder],nums[seeker]
                holder += 1
            seeker += 1
        