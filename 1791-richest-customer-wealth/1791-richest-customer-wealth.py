class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            total = sum(account)
            richest = max(richest,total)
        return richest
            

        