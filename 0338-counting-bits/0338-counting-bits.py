class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]
        for i in range(n+1):
            binary_str = bin(i)
            ans[i] = binary_str.count("1")
        return ans
            