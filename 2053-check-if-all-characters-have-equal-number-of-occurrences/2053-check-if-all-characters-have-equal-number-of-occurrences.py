class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        count_no = count[s[0]]
        print(count_no)
        for num,its_count in count.items():
            if its_count != count_no:
                return False
        return True
        