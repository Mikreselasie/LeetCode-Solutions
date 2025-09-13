class Solution(object):
    def maxFreqSum(self, s):
        vowels = dict()
        consonants = dict()

        for char in s:
            if char == "a":
                if "a" in vowels:
                    vowels["a"] += 1
                else:
                    vowels["a"] = 1
            elif char == "e":
                if "e" in vowels:
                    vowels["e"] += 1
                else:
                    vowels["e"] = 1
            elif char == "i":
                if "i" in vowels:
                    vowels["i"] += 1
                else:
                    vowels["i"] = 1
            elif char == "o":
                if "o" in vowels:
                    vowels["o"] += 1
                else:
                    vowels["o"] = 1
            elif char == "u":
                if "u" in vowels:
                    vowels["u"] += 1
                else:
                    vowels["u"] = 1
            else:
                if char in consonants:
                    consonants[char] += 1
                else:
                    consonants[char] = 1
        vowel_max = 0
        cons_max = 0

        for x,y in vowels.items():
            vowel_max = max(vowel_max,y)
        for x,y in consonants.items():
            cons_max = max(cons_max,y)
        return cons_max + vowel_max
        
        