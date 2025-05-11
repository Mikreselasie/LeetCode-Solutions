class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left = 0

        for right in range(len(arr)):
            if right - left + 1 > 2 and arr[right]%2: return True
            if arr[right]%2 == 0: left = right + 1
        
        return False