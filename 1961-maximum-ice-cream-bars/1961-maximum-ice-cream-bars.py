class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorter = [0]*100000

        for cost in costs:
            sorter[cost-1] += 1
        count = 0
        for no in range(len(sorter)):
            while coins > 0 and sorter[no] > 0:
                coins -= (no+1)
                if coins >= 0:
                    count += 1
                sorter[no] -= 1
        return count


        