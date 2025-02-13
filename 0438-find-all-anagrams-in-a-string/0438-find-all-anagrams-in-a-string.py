class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)

        left = 0
        right = len(p)
        answer = []
        temp_count = Counter(s[left:right])
        if temp_count == p_count:
            answer.append(left)
        for i in range(right,len(s)):
            print("LOOP:",i-right+1,temp_count)
            temp_count[s[i]] = temp_count.get(s[i],0) + 1

            temp_count[s[left]] -= 1
            if temp_count[s[left]] == 0:
                del temp_count[s[left]]
            left += 1
            if temp_count == p_count:
                answer.append(left)
        return answer

