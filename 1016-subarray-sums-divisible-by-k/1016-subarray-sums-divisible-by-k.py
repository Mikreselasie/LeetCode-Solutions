class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1

        running = 0
        count = 0
        for num in nums:
            running += num 
            if running%k in my_dict:
                count += my_dict[running%k]
            my_dict[running%k] += 1
        return count      