class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for num in range(low,high+1):
            num_str = str(num)
            if len(num_str)%2:
                continue
            left = num_str[:len(num_str)//2]
            tempL = 0
            right = num_str[len(num_str)//2:]
            tempR = 0
            for n in left:
                tempL += int(n)
            for m in right:
                tempR += int(m)   
            if tempL == tempR:
                cnt += 1
        return cnt         
        