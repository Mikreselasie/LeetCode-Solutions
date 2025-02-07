class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        my_dict = {}
        for word in strs:
            tup = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            counter = Counter(word)
            for i, j in counter.items():
                ord_v = ord(i)-97
                tup[ord_v] = j

            tupled = tuple(tup)
            my_dict[tupled] = my_dict.get(tupled, []) + [word]

        for count,words in my_dict.items():
            anagrams.append(words)

        return anagrams
       