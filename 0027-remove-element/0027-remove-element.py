class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i < len(nums):
            if nums[i] == val:
                nums[i],nums[-1] = nums[-1],nums[i]
                nums.pop()
                i -= 1
            i += 1

        return len(nums)
        