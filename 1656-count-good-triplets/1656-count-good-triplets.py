class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(len(arr)):
            for j in range(1+i,len(arr)):
                for k in range(1+j,len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[i]-arr[k]) <= c and abs(arr[j]-arr[k]) <= b: 
                        cnt += 1
        return cnt

        