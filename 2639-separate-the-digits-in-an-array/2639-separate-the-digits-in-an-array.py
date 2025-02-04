class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        str_store = []
        new_list = []
        for i in nums:
            str_store.append(str(i))
        for j in str_store:
            for k in range(len(j)):
                new_list.append(int(j[k]))

        return new_list

        