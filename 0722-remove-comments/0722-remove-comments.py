class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        opened = False
        comment_pt = 0
        lines = 0
        without_comment = []
        temp = ""  
        while lines < len(source):
            i = 0
            while i < len(source[lines]):
                if opened:
                    if i + 1 < len(source[lines]) and source[lines][i] == '*' and source[lines][i + 1] == '/':
                        opened = False
                        i += 1  
                else:
                    if i + 1 < len(source[lines]) and source[lines][i] == '/' and source[lines][i + 1] == '*':
                        opened = True
                        i += 1  
                    elif i + 1 < len(source[lines]) and source[lines][i] == '/' and source[lines][i + 1] == '/':
                        break  
                    else:
                        temp += source[lines][i]

                i += 1
            if temp and not opened:
                without_comment.append(temp)
                temp = "" 

            lines += 1

        return without_comment
