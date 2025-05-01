class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        negative = 0
        if x < 0: negative = True
        x = abs(x)
        while x:
            num = num*10 + x%10
            x //= 10
        if negative : num = -num

        if num >= pow(2,31) or num < pow(-2,31):
            return 0
        return num
        