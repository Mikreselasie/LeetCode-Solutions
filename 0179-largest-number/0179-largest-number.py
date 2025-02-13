class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums)):
            for j in range(1,len(nums)-i):
                if str(nums[j]) + str(nums[j-1]) > str(nums[j-1]) + str(nums[j]):
                    nums[j],nums[j-1] = nums[j-1],nums[j]

        return str(int("".join(str(num) for num in nums)))