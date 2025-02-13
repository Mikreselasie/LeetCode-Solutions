class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        
        max_len = 0
        
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[i])
            max_len = max(max_len,len(my_set))

        return max_len
        