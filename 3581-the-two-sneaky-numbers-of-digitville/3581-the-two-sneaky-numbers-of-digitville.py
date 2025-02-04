class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counted_list = Counter(nums)
        new_list = []

        for num,count in counted_list.items():
            if count > 1:
                new_list.append(num)
        return new_list
        