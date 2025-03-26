class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)
        nums.sort()
        median = nums[len(nums)//2]
        count = 0

        for num in nums:
            if abs(num - median) % x !=0:
                return -1 
            count += abs(num - median)//x
        return count    