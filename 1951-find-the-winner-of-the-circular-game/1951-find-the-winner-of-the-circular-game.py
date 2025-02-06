class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        count = 0

        removed_ppl = set()
        while len(friends)-len(removed_ppl)-1:
            for i in friends:
                if i not in removed_ppl:
                    count += 1
                    if count == k:
                        count = 0
                        removed_ppl.add(i)
                        if len(friends)-len(removed_ppl) == 1:
                            break
        for i in friends:
            if i not in removed_ppl:
                return i

        
                



        