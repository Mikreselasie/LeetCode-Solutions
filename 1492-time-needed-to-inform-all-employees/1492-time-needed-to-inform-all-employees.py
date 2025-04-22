class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1: return 0
        my_dict = defaultdict(list)

        for i in range(len(manager)):
            my_dict[manager[i]].append(i)
        
        gonee = 0
        def dfs(node,gone):
            nonlocal gonee
            if informTime[node] == 0:
                return gone
            gone += informTime[node]

            for val in my_dict[node]:
                gonee = max(gonee, dfs(val,gone))
            return gonee
        
        return dfs(my_dict[-1][0],0)