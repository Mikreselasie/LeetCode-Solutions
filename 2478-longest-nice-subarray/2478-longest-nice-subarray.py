class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0  # Stores bitwise OR of the current window
        left = 0
        ans = 0

        for right in range(len(nums)):
            while (used_bits & nums[right]) != 0:  # If conflict, move left pointer
                used_bits ^= nums[left]  # Remove nums[left] from window
                left += 1  # Shrink window from left

            used_bits |= nums[right]  # Add nums[right] to window
            ans = max(ans, right - left + 1)  # Update longest nice subarray length

        return ans
