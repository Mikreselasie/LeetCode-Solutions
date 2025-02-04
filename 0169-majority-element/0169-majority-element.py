class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)/2

        nums_count = Counter(nums)
        nums_sort = sorted(nums_count.items(),key = lambda item: item[1],reverse = True)

        return nums_sort[0][0]
        