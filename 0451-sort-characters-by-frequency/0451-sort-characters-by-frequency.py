class Solution:
    def frequencySort(self, s: str) -> str:
        counted = Counter(s)
        sorted_dict_desc = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))
        my_list = []
        for char,count in sorted_dict_desc.items():
            my_list.append(char* count)
        return "".join(my_list)
        