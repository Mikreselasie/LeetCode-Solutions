class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(x):
            y = 1
            while x > 1:
                y *= x
                x -= 1
            return y
        a = factorial(n)
        ans = 0
        while a%10 == 0:
            ans += 1
            a //= 10
        return ans