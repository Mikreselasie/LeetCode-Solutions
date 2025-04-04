class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ptr = 0
        while ptr < len(nums):
            if nums[ptr]-1 == ptr or nums[nums[ptr]-1] == nums[ptr] : ptr += 1
            else: nums[nums[ptr]-1],nums[ptr] = nums[ptr],nums[nums[ptr]-1]
        
        ans = []
        for i in range(len(nums)):
            if nums[i]!= i+1:
                ans.append(nums[i])
                ans.append(i+1)
        return ans