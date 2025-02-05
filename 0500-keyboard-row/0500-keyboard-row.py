class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = ("q","w","e","r","t","y","u","i","o","p")
        row_2 = ("a","s","d","f","g","h","j","k","l")
        row_3 = ("z","x","c","v","b","n","m")
        current_row = ()
        truth = True
        store_list = []
        for word in words:
            word1 = word.lower()
            if word1[0] in row_1:
                current_row = row_1
            elif word1[0] in row_2:
                current_row = row_2
            else:
                current_row = row_3
            for char in word1:
                if char not in current_row:
                    truth = False
                    break
                else:
                    truth = True
            if truth:
                store_list.append(word)
            
        return store_list



                

        