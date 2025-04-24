from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        n = len(nums)
        ans = 0

        freq = defaultdict(int)
        left = 0

        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) == total_unique:
                ans += n - right  
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return ans
