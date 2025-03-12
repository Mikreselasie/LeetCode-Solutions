class Solution:
    def myPow(self, x: float, n: int) -> float:
        my_dict = dict()
        def pow(x,m):
            if m == 1: return x
            if m == 0: return 1
            if ceil(m/2) not in my_dict: my_dict[ceil(m/2)] = pow(x,ceil(m/2))
            if m//2 not in my_dict: my_dict[m//2] = pow(x,m//2)

            return my_dict[ceil(m/2)] * my_dict[m//2] 

        ans = pow(x,abs(n))
        if n < 0:
            return 1/ans
        return ans