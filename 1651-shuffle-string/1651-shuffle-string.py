class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index_to_char_dict = {}
        
        for i in range(len(s)):
            index_to_char_dict[indices[i]] = s[i]
        sorted_dict = sorted(index_to_char_dict.items(), key=lambda x: x[0])
        word = []
        for index,char in sorted_dict:
            word.append(char)
        return "".join(word)

        