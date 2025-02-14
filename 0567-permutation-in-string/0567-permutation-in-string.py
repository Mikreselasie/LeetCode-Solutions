class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        width = len(s1)
        left = 0
        s1_count = Counter(s1)
        right = width
        temp_s2 = Counter(s2[:right])

        if temp_s2 == s1_count:
            return True

        while right < len(s2):
            temp_s2[s2[right]] = temp_s2.get(s2[right], 0) + 1
            temp_s2[s2[left]] -= 1
            if temp_s2[s2[left]] == 0:
                del temp_s2[s2[left]]
            left += 1
            right += 1
            
            if temp_s2 == s1_count:
                return True
            
        return False
