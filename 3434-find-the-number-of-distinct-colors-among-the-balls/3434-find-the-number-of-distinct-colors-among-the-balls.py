class Solution(object):
    def queryResults(self, limit, queries):
        bal = {}
        col = defaultdict(int)
        n = len(queries)
        res = [0] * n

        for i in range(n):
            key = queries[i][0]
            value = queries[i][1]

            if key not in bal:
                bal[key] = value
            else:
                oldBalance = bal[key]
                if col[oldBalance] == 1:
                    del col[oldBalance]
                else:
                    col[oldBalance] -= 1
                bal[key] = value

            col[value] += 1
            res[i] = len(col)

        return res