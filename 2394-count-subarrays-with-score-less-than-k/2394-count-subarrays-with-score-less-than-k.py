class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        running = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            running += nums[right]
            while running * (right-left+1) >= k:
                running -= nums[left] 
                left += 1
            
            ans += right - left + 1
        
        return ans

        
        