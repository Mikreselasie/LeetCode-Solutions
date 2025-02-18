from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1
        prefix = 0

        for idx in range(len(nums)):
            prefix += nums[idx]
            
            diff = prefix - k
            res += prefix_dict.get(diff,0)
            prefix_dict[prefix] = 1 + prefix_dict.get(prefix,0)
    
        return res