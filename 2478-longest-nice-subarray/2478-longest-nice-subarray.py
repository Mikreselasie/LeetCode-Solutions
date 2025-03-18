class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            while (used_bits & nums[right]) != 0:
                used_bits = used_bits ^ nums[left]
                left += 1
            used_bits = used_bits | nums[right]
            ans = max(ans,right-left + 1)
        return ans