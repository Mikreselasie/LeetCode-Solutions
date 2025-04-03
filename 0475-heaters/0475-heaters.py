from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        ptr1 = 0  # Pointer for houses
        ptr2 = 0  # Pointer for heaters
        radius = 0

        while ptr1 < len(houses):  
            # Find the closest heater for the current house
            while ptr2 < len(heaters) - 1 and abs(heaters[ptr2 + 1] - houses[ptr1]) <= abs(heaters[ptr2] - houses[ptr1]):
                ptr2 += 1  # Move to the next heater if it's closer
            
            # Calculate the min distance to the nearest heater
            temp_rad = abs(heaters[ptr2] - houses[ptr1])
            radius = max(radius, temp_rad)  # Keep track of the max radius required
            ptr1 += 1  # Move to the next house

        return radius
