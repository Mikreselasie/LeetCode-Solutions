class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def flipper(num):
            if num == 0:
                return 1
            else:
                return 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0 and i < len(nums)-2:
                for j in range(i,i+3):
                    nums[j] = flipper(nums[j])
                count += 1
            elif nums[i] == 0 and i >= len(nums)-2:
                return -1
        return count            
