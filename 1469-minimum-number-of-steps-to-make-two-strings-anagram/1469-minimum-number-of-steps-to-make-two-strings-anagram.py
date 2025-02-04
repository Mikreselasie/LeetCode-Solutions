class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # t_count = Counter(t)
        # s_count = Counter(s)

        # t_count_sorted = sorted(x.items, key = lambda item: item[0])
        # s_count_sorted = sorted(x.items, key = lambda item: item[0])
        return sum((Counter(t)-Counter(s)).values())


        