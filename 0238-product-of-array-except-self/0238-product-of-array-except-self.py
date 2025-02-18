class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running = 1
        switch = False
        not_running = 0
        for num in nums:
            if num == 0:
                switch = True
                not_running += 1
                continue
            running *= num
        for i in range(len(nums)): 
            if nums[i] == 0:
                if not_running >= 2:
                    continue
                nums[i] = running
                continue
            if not switch:
                nums[i] = running//nums[i]
            else:
                nums[i] = 0
        return nums
        