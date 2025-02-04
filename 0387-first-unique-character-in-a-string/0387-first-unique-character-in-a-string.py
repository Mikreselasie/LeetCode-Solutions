class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)

        for i in range(len(s)):
            if x[s[i]] == 1:
                return i
        return -1
        