from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = len(s) - 1
        my_list = []
        
        while left <= len(s) - 1:
            while s[left] != s[right]:
                right -= 1
            
            temp_left = right
            temp_right = right
            
            x = left+1
            while x < temp_left:
                for i in range(len(s) - 1, temp_left, -1):
                    if s[x] == s[i]:
                        temp_right = max(temp_right, i)  # Ensure temp_right is updated correctly
                        temp_left = i
                        break
                x += 1
            print("TEMP-RIGHT",temp_right)
            my_list.append(temp_right + 1 - left)
            left = temp_right + 1  # Update left correctly to avoid infinite loops
            right = len(s) - 1  # Reset right pointer
        
        return my_list
