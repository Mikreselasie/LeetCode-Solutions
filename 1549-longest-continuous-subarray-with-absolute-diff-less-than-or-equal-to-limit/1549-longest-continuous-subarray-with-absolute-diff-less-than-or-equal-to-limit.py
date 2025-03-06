class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = deque()
        inc = deque()
        left = 0
        ans = float("-inf")
        for right in range(len(nums)):
            while dec and dec[-1] < nums[right]:
                dec.pop()
            while inc and inc[-1] > nums[right]:
                inc.pop()
            dec.append(nums[right])
            inc.append(nums[right])

            while dec[0] -  inc[0] > limit:
                val = nums[left]
                if val == inc[0]:
                    inc.popleft()
                if val == dec[0]:
                    dec.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans
