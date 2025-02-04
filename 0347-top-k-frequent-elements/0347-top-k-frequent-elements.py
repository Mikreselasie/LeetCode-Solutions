class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)

        sorted_dict = sorted(counted.items(),key = lambda item: item[1],reverse = True)
        my_list = []
        for i in range(k):
            my_list.append(sorted_dict[i][0])
        return my_list

        