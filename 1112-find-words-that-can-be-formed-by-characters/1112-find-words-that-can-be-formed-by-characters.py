class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        length = 0
        for i in words:
            new_count = Counter(i)
            if chars_count > new_count:
                length += len(i)
        return length
        
        