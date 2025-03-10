class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a","e","i","o","u"}
        ans = 0
        for i in range(len(word)):
            temp_set = set()
            count = 0
            if word[i] in vowels:
                right = i
                while right < len(word) and word[right] in vowels:
                    temp_set.add(word[right])
                    if len(temp_set) == 5:
                        ans += 1
                    right += 1
        return ans
        