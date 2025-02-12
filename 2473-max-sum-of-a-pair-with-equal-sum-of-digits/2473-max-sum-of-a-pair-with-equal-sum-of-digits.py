class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in range(len(nums)):
            temp_no = str(nums[i])
            temp_list = list(map(int,temp_no))
            temp_sum = sum(temp_list)
            if temp_sum not in my_dict:
                my_dict[temp_sum] = []
            my_dict[temp_sum].append(nums[i])
        max_num = 0

        for summed,listed in my_dict.items():
            if len(listed) >= 2:
                listed.sort()
                my_sum = listed[-1] + listed[-2]
                max_num = max(max_num,my_sum)
        print(my_dict)
        if max_num == 0:
            return -1
        else:
            return max_num