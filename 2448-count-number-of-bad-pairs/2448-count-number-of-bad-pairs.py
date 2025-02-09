class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total  = (len(nums)* (len(nums)-1))//2
        good = 0
        for i in range(len(nums)):
            difference = nums[i] - i
            freq[difference] += 1

        for i in freq.values():
            if i >= 2:
                good += (i *(i-1))//2
        return total - good
