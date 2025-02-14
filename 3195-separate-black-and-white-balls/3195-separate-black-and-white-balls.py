class Solution:
    def minimumSteps(self, s: str) -> int:
        #  11000111
        right = len(s)-1 
        cnt = 0
        for left in range(len(s)-1,-1,-1):
            if s[left] == "1":
                cnt += right - left
                right -= 1
        return cnt

