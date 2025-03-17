class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)

        for num,count in nums_counter.items():
            if count%2 == 1:
                return False
        return True