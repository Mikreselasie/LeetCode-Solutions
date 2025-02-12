class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        temp_list = []
        for num in nums:
            x = nums_sorted.index(num)
            temp_list.append(x)
        return temp_list


        