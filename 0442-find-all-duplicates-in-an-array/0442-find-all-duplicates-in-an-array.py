class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        my_list = []
        for num,count in counted.items():
            if count == 2:
                my_list.append(num)

        return my_list
        