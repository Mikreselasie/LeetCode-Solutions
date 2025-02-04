class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        nums_sort = sorted(nums_count.items(),key = lambda item: item[1],reverse = True)

        return nums_sort[0][0]
        