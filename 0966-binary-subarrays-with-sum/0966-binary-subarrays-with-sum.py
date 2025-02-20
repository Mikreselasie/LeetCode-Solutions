class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = defaultdict(int)

        my_dict[0] = 1

        count = 0
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            if running - goal in my_dict:
                count += my_dict[running - goal]
            my_dict[running] += 1
        return count
