from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(count_t,window):
            for char in count_t:
                if count_t[char] > window[char]:
                    return False
            return True
        t_count = Counter(t)
        t_len = len(t)
        window = Counter()
        my_list = list()
        left = 0
        ans = [float("-inf"),float("inf")]

        for right in range(len(s)):
            window[s[right]] += 1
            while valid(t_count,window):
                if right - left < ans[1] - ans[0]:
                    ans = [left,right]
                window[s[left]] -= 1
                left += 1
        if ans[0] == float("-inf"):
            return ""
        return s[ans[0]:ans[1] + 1]




        # for right in range(len(s)):
        #     if s[right] in t_count:
        #         s_count[s[right]] += 1
        #         while s_count[s[right]] > t_count[s[right]]:
        #             if s[left] in t_count:
        #                 s_count[s[left]] -= 1
        #             left -= 1
        #     print(s_count, "LOOP:",right)
        #     while s_count == t_count:
        #         my_list.append(s[left:right+1])
        #         s_count[s[left]] -= 1
        #         if s_count[s[left]] == 0:
        #             del s_count[s[left]]
        #         left += 1

        # print(my_list)

            
        