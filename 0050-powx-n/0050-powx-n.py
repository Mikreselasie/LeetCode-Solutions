class Solution:
    def myPow(self, x: float, n: int) -> float:
        my_dict = dict()
        if n == 1:
            return x
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        def pow(x,n):
            if n == 1:
                return x
            if ceil(n/2) not in my_dict: my_dict[ceil(n/2)] = pow(x, ceil(n/2))
            if n//2 not in my_dict: my_dict[n//2] = pow(x, n//2)
            return my_dict[ceil(n/2)]*my_dict[n//2]
        answer = pow(x,abs(n))
        if n < 0:
            return 1/answer
        return answer