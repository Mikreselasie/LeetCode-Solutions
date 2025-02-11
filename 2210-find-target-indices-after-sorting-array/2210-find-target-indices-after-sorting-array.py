class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        sorter = [0] * 100

        for num in nums:
            sorter[num-1] += 1
        new_list = []
        for idx in range(100):
            for i in range(sorter[idx]):
                new_list.append(idx+1)
        indexes = []
        for i in range(len(new_list)):
            if new_list[i] == target:
                indexes.append(i)
        return indexes
        