class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_dict = {}
        words_list = []

        for i in list1:
            if i in list1 and i in list2:
                index_dict[i] = index_dict.get(i,0) + list1.index(i)

        for j in list2:
            if j in list1 and j in list2:
                index_dict[j] = index_dict.get(j,0) + list2.index(j)

        min_no = min(index_dict.values())
        
        for word,count in index_dict.items():
            if count == min_no and (word in list1 and word in list2) :
                words_list.append(word)
        print(words_list)
        return words_list        