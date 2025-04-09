class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        if nums[0] < k: return -1
        return len(nums) - (nums.index(k)+1) if k in nums else len(nums)