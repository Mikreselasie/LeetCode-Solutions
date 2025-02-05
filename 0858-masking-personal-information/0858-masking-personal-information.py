class Solution:
    def maskPII(self, s: str) -> str:
        my_str = ""
        s = s.lower()
        if s[-1].isalpha():
            for i in s:
                if i == "@":
                    index = s.index(i)
            my_str += s[0].lower() + "*****" + s[index -1:]
        else:
            symbol_set = {'+', '-', '(', ')', ' '}

            new_str = []
            for j in s:
                if j not in symbol_set:
                    new_str.append(j)
            if len(new_str) == 10:
                my_str += "***-***-" + "".join(new_str[-4:])
            elif len(new_str) == 11:
                my_str += "+*-***-***-" + "".join(new_str[-4:])
            elif len(new_str) == 12:
                my_str += "+**-***-***-" + "".join(new_str[-4:])
            else:
                my_str += "+***-***-***-" + "".join(new_str[-4:])

        return my_str        