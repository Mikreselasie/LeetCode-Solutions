class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNo = max(nums)
        left = 0
        cnt = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == maxNo : cnt += 1

            while cnt >= k: 
                if nums[left] == maxNo : cnt -= 1
                left += 1
                ans += len(nums) - right
        return ans
        