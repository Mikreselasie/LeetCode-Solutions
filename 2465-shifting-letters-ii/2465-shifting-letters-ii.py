class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        my_array = [0]*len(s)
        for left,right,direction in shifts:
            if direction:
                my_array[left] += 1
                if right < len(s)-1:
                    my_array[right+1] -= 1
            else:
                my_array[left] -= 1
                if right < len(s)-1:
                    my_array[right+1] += 1
        my_str_list = [0]*len(s)
        for char_idx in range(len(s)):
            if char_idx > 0:
                my_array[char_idx] += my_array[char_idx-1]
            my_str_list[char_idx] = (ord(s[char_idx]) + my_array[char_idx]-97)%26 + 97
        for idx in range(len(s)):
            my_str_list[idx] = chr(my_str_list[idx])
        return "".join(my_str_list)

        

        