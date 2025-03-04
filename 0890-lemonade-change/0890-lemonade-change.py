from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()  
        for bill in bills:
            if bill == 5:
                counter[5] += 1  
            elif bill == 10:
                if counter[5] == 0:  
                    return False
                counter[5] -= 1  
                counter[10] += 1  
            elif bill == 20:
                if counter[10] > 0 and counter[5] > 0:  
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:  
                    counter[5] -= 3
                else:
                    return False  
                counter[20] += 1  

        return True