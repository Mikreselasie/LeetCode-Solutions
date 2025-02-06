class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        store = list(allowed)
        
        count = 0
        for word in words:
            truth = True
            for char in word:
                if char not in store:
                    truth = False
                    break
            if truth:
                count += 1

        return count

