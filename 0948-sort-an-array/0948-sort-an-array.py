class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        my_list = [0] * 100001
        total_list = []
        for num in nums:
            my_list[num+50000] += 1
        for idx in range(len(my_list)):
            for i in range(my_list[idx]):
                total_list.append(idx-50000)
        return total_list
        