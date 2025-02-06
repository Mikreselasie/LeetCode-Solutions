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
                print(truth)
            if truth:
                count += 1
        print(store)
        return count

