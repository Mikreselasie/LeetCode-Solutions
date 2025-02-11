class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        sorter = [0] * 100000
        new_list = []
        for idx in range(len(heights)):
            sorter[heights[idx]-1] = names[idx]
        for name in sorter:
            if name != 0:
                new_list.append(name)
        
        return list(reversed(new_list))



        # for i in range(len(heights)):
        #     for j in range(len(heights) - i -1):
        #         if heights[j] < heights[j+1]:
        #             heights[j],heights[j+1] = heights[j+1],heights[j]
        #             names[j],names[j+1] = names[j+1],names[j]

        