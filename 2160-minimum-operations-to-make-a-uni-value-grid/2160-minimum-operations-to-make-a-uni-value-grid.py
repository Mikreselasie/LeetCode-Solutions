class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        
        nums.sort()
        mid_no = nums[len(nums)//2]
        count = 0 

        for num in nums:
            if abs(num - mid_no) % x:
                return -1
            count += abs(num - mid_no) // x
        return count
        