class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        width = len(part)
        i = 0
        while i < len(s):
            if s[i:i+width] == part:
                s = s[:i] + s[i+width:]
                i = 0
            else:
                i += 1
        return s
