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
            # for char in word:
            #     tup[ord_v] += 1
            my_dict[tupled] = my_dict.get(tupled, []) + [word]

        for count,words in my_dict.items():
            anagrams.append(words)

        return anagrams
        # anagrams_paired = []
        # dont_consider = []
        # for i in range(len(strs)):
        #     anagrams = []
        #     count1 = Counter(strs[i])
        #     for j in range(i,len(strs)):
        #         if Counter(strs[j]) == count1 and j not in dont_consider:
        #             anagrams.append(strs[j])
        #             dont_consider.append(j)

        #     if anagrams == []:
        #         continue
        #     else:
        #         anagrams_paired.append(anagrams)
        # return anagrams_paired     

        

        