class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                temp1 = s[:right] + s[right + 1:]
                temp2 = s[:left] + s[left + 1:]
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]
            right -= 1
            left += 1
        return True
