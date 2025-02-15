class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, index, current_sum):
            if index == len(s):
                return current_sum == target
            for i in range(index, len(s)):
                num = int(s[index:i+1])
                if can_partition(s, target, i+1, current_sum + num):
                    return True
            return False
        
        result = 0
        for i in range(1, n+1):
            square = str(i * i)
            if can_partition(square, i, 0, 0):
                result += i * i
        return result