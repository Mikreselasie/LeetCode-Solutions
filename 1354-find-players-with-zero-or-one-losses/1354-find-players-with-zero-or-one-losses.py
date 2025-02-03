class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set(x[0] for x in matches)
        losers = set(x[1] for x in matches)

        # Identify all-time winners by set difference
        all_time_winners = sorted(winners - losers)

        # Count losses efficiently
        losers_dict = {}
        for winner, loser in matches:
            losers_dict[loser] = losers_dict.get(loser, 0) + 1

        # Find one-time losers
        one_time_losers = sorted([person for person, no_of_losses in losers_dict.items() if no_of_losses == 1])

        return [all_time_winners, one_time_losers]