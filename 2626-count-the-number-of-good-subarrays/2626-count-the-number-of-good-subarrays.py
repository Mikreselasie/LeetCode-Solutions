class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        ans = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1
            count += freq[nums[right]] - 1  # New pairs added

            while count >= k:
                ans += len(nums) - right  # all subarrays from left to right are valid
                freq[nums[left]] -= 1
                count -= freq[nums[left]]  # Pairs removed
                left += 1

        return ans
