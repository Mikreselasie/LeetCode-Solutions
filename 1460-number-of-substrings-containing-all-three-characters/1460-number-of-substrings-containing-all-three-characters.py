class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        chars = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            chars[s[right]] += 1
            while len(chars) == 3:
                ans += len(s) - right
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1
        return ans


        