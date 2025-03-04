class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        ptr = 0
        while ptr < len(s):
            counter = Counter()
            counter[s[ptr]] = 1
            while ptr < len(s)-1 and counter["L"] != counter["R"]:
                ptr += 1
                counter[s[ptr]] += 1
            count += 1
            ptr += 1
        return count