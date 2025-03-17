class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_counted = Counter(nums)

        for val,count in nums_counted.items():
            if count %2 :
                return False
        return True