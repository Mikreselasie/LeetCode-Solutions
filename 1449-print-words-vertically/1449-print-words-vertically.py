class Solution:
    def printVertically(self, s: str) -> List[str]:
        str_store  = s.split()
        length = 0
        new_list = []
        for i in str_store:
            length = max(length,len(i))
        print(length)
        for j in range(length):
            temp_word = ""
            for word in str_store:
                if j < len(word):
                    temp_word += word[j]
                else:
                    temp_word += " "
            new_list.append(temp_word.rstrip())
        return new_list
