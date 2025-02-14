from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        left = 0
        my_word = ""

        for right in range(len(s)):
            if s[right] in t_count:
                s_count[s[right]] += 1
            while all(s_count[char] >= t_count[char] for char in t_count):
                substring = s[left:right+1]
                if not my_word or len(substring) < len(my_word):
                    my_word = substring  
                if s[left] in t_count:
                    s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1
        return my_word if my_word else ""

            
        