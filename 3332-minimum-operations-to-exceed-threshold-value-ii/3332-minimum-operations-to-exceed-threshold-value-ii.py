import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert list to a min-heap
        count = 0
        
        while nums[0] < k and len(nums) > 1:
            smallest = heapq.heappop(nums)
            second_smallest = heapq.heappop(nums)
            new_element = smallest * 2 + second_smallest
            heapq.heappush(nums, new_element)
            count += 1
        
        return count if nums[0] >= k else -1  # Return -1 if it's not possible to achieve k