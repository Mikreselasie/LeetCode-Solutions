class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        string = "1"

        def countAndSay(string):
            new = []

            left = 0
            for right in range(len(string)):
                if string[right] != string[left]:
                    new.append(string[left:right])
                    left = right
                if right == len(string)-1:
                    new.append(string[left:])
            
            word = []

            for i in new:
                word.append(str(len(i)) + i[0])
            return "".join(word)
        
        for i in range(1,n):
            string = countAndSay(string)
        return string

        