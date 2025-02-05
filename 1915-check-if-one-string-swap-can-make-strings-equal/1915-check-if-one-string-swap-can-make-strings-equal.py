class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        difference  = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference += 1
                print(difference)
                if difference > 2:
                    return False
        return True
