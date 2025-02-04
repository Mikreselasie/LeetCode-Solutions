class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        nums_sort = list(sorted(nums_count.items(),key = lambda item: item[1],reverse = True))

        print(nums_sort)
        return [i[0] for i in filter(lambda item: item[1] > len(nums)//3, nums_sort)]
        