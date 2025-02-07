class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum(x for x in nums if x % 2 == 0)
        result = []
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sum_even -= nums[idx]
            
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                sum_even += nums[idx]
                
            result.append(sum_even)
        
        return result