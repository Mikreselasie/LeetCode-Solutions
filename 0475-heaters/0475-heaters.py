from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        ptr1 = 0  
        ptr2 = 0  
        radius = 0

        while ptr1 < len(houses):     
            while ptr2 < len(heaters) - 1 and abs(heaters[ptr2 + 1] - houses[ptr1]) <= abs(heaters[ptr2] - houses[ptr1]):
                ptr2 += 1 
            
            
            temp_rad = abs(heaters[ptr2] - houses[ptr1])
            radius = max(radius, temp_rad)  
            ptr1 += 1 

        return radius
