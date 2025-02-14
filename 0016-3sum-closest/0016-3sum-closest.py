class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                summed = nums[left] + nums[right] + nums[i]
                if summed > target:
                    right -= 1
                elif summed < target:
                    left += 1
                else:
                    return target
                if abs(summed - target) < abs(ans - target):
                    ans = summed
            
                
        return ans