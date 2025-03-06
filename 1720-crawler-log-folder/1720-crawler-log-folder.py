class Solution:
    def minOperations(self, logs: List[str]) -> int:
        a = 0

        for log in logs:
            if log == "../":
                if a:
                    a -= 1
            elif log == "./":
                continue
            else:
                a += 1
        return a