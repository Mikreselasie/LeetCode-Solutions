class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(2,len(nums)):
            if nums[i-1] == ((nums[i] + nums[i-2])*2):
                cnt += 1
        return cnt