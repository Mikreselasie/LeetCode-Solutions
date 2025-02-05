class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index_to_char_dict = {}
        
        for i in range(len(s)):
            index_to_char_dict[indices[i]] = s[i]
        
        word = []
        for i in range(len(indices)):
            word.append(index_to_char_dict[i])
        return "".join(word)

        