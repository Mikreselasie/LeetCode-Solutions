class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def word(n):
            if n == 1:
                return "0"
            
            a = []
            for char in word(n-1):
                if char == "1": a.append("0")
                else: a.append("1")
            return word(n-1) + "1" + "".join(a[::-1])
        return word(n)[k-1]


        