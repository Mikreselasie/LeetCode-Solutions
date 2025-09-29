class Solution(object):
    def change(self, amount, coins):
        
        memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(memo) - 1, -1, -1):
            for j in range(len(memo[0]) - 1, -1, -1):
                right = memo[i][j + coins[i]] if j + coins[i] <= amount else 0
                down = memo[i + 1][j] if i + 1 != len(coins) else j == amount
                memo[i][j] = right + down
        return memo[0][0]


         