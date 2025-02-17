from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_count = defaultdict(int)  
        prefix_count[0] = 1  
        count = 0

        for num in nums:
            prefix_sum += num  
            
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k] 

            prefix_count[prefix_sum] += 1

        return count
